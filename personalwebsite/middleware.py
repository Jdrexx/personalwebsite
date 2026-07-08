"""Custom security middleware for CSP, Permissions-Policy, and related headers."""


class SecurityHeadersMiddleware:
    """Adds Content-Security-Policy and Permissions-Policy headers.

    CSP uses 'unsafe-inline' for scripts because the site has inline
    scripts for theme toggling, terminal, counters, and JSON-LD injection.
    Long-term improvement: move all inline scripts to static JS files
    so 'unsafe-inline' can be removed.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Content-Security-Policy
        csp = (
            "default-src 'self';"
            "script-src 'self' 'unsafe-inline';"
            "style-src 'self' https://fonts.googleapis.com;"
            "font-src 'self' https://fonts.gstatic.com;"
            "img-src 'self' data:;"
            "form-action https://formspree.io;"
            "base-uri 'self';"
            "frame-ancestors 'none';"
        )
        response["Content-Security-Policy"] = csp

        # Permissions-Policy — disable unused powerful features
        response["Permissions-Policy"] = (
            "camera=(), microphone=(), geolocation=(), interest-cohort=()"
        )

        return response
