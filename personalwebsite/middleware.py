"""Custom security middleware for CSP, Permissions-Policy, and related headers."""


class SecurityHeadersMiddleware:
    """Adds Content-Security-Policy and Permissions-Policy headers.

    Interactive code is served from versioned static files, so executable
    inline scripts are not permitted. JSON-LD is inert metadata.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Content-Security-Policy
        csp = (
            "default-src 'self';"
            "script-src 'self' https://www.googletagmanager.com;"
            "connect-src 'self' https://www.google-analytics.com https://*.google-analytics.com;"
            "style-src 'self';"
            "font-src 'self';"
            "img-src 'self' data: https://www.google-analytics.com;"
            "form-action 'self' https://formspree.io;"
            "base-uri 'self';"
            "frame-ancestors 'none';"
        )
        response["Content-Security-Policy"] = csp

        # Permissions-Policy — disable unused powerful features
        response["Permissions-Policy"] = (
            "camera=(), microphone=(), geolocation=(), interest-cohort=()"
        )

        return response
