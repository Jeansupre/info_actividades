import getpass
import json
from dataclasses import dataclass, field
from http.cookiejar import CookieJar
from urllib.error import HTTPError, URLError
from urllib.request import (
    HTTPCookieProcessor,
    OpenerDirector,
    Request,
    build_opener,
)


LOGIN_URL = "https://gestion.uis.edu.co/auth/api/auth/login"
USER_URL = "https://gestion.uis.edu.co/auth/api/users/user"


class PortalAuthenticationError(RuntimeError):
    """Indica que no fue posible autenticar al usuario en el portal."""


class PortalRequestError(RuntimeError):
    """Indica que una petición al portal no pudo completarse."""


def _detalle_error(error: HTTPError) -> str:
    """Obtiene el detalle del servidor sin imprimir credenciales."""
    try:
        body = error.read().decode("utf-8", errors="replace").strip()
    except OSError:
        return ""
    return f" Detalle del servidor: {body}" if body else ""


@dataclass
class PortalSession:
    token: str
    _opener: OpenerDirector = field(repr=False, compare=False)
    idPersona: int | str | None = None
    idUsuario: int | str | None = None

    def obtener_datos_usuario(self, user_url: str = USER_URL) -> None:
        """Consulta y guarda los identificadores del usuario en esta sesión."""
        request = Request(
            user_url,
            headers={
                "Accept": "application/json",
                "Authorization": f"Bearer {self.token}",
            },
            method="GET",
        )

        try:
            with self._opener.open(request, timeout=30) as response:
                response_body = json.loads(response.read().decode("utf-8"))
        except HTTPError as error:
            raise PortalRequestError(
                f"El portal rechazó la consulta del usuario (HTTP {error.code})."
                f"{_detalle_error(error)}"
            ) from error
        except URLError as error:
            raise PortalRequestError(
                f"No fue posible consultar el usuario: {error.reason}."
            ) from error
        except (UnicodeDecodeError, json.JSONDecodeError) as error:
            raise PortalRequestError(
                "El portal devolvió una respuesta inválida al consultar el usuario."
            ) from error

        if not isinstance(response_body, dict):
            raise PortalRequestError(
                "La respuesta del usuario no tiene el formato esperado."
            )
        if "ID_PERSONA" not in response_body or "ID" not in response_body:
            raise PortalRequestError(
                "La respuesta del usuario no contiene ID_PERSONA e ID."
            )

        self.idPersona = response_body["ID_PERSONA"]
        self.idUsuario = response_body["ID"]
        print("Datos del usuario obtenidos correctamente")


def autenticar(
    username: str,
    password: str,
    login_url: str = LOGIN_URL,
) -> PortalSession:
    """Autentica y conserva las cookies de la sesión únicamente en memoria."""
    if not username:
        raise ValueError("El nombre de usuario no puede estar vacío.")
    if not password:
        raise ValueError("La contraseña no puede estar vacía.")

    body = json.dumps(
        {"nombre_usuario": username, "password": password}
    ).encode("utf-8")

    request = Request(
        login_url,
        data=body,
        headers={"Content-Type": "application/json", "Accept": "application/json"},
        method="POST",
    )
    
    cookie_jar = CookieJar()
    opener = build_opener(HTTPCookieProcessor(cookie_jar))

    try:
        with opener.open(request, timeout=30) as response:
            response_body = json.loads(response.read().decode("utf-8"))
    except HTTPError as error:
        raise PortalAuthenticationError(
            f"El portal rechazó la autenticación (HTTP {error.code})."
            f"{_detalle_error(error)}"
        ) from error
    except URLError as error:
        raise PortalAuthenticationError(
            f"No fue posible conectar con el portal: {error.reason}."
        ) from error
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise PortalAuthenticationError(
            "El portal devolvió una respuesta inválida."
        ) from error

    token = response_body.get("token") if isinstance(response_body, dict) else None
    if not isinstance(token, str) or not token:
        raise PortalAuthenticationError(
            "La respuesta del portal no contiene un token válido."
        )

    return PortalSession(token=token, _opener=opener)


def autenticar_interactivamente() -> PortalSession:
    """Solicita las credenciales y crea una sesión en memoria."""
    username = input("Usuario del portal: ").strip()
    password = getpass.getpass("Contraseña del portal: ")
    return autenticar(username, password)
