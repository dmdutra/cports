pkgname = "k6"
pkgver = "0.54.0"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Modern load testing tool, using Go and Javascript"
maintainer = "Gabriel M. Dutra <dmdutra@proton.me>"
license = "AGPL-3.0-only"
url = "https://github.com/grafana/k6"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "706089f6dd65b8e50cee71ac30d32b44be8ddb6c65acf8ff54b6a0729027148e"
# k6 tests requires network connection
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.md")
