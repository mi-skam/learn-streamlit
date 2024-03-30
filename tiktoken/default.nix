{ pkgs }:
let
  pname = "tiktoken";
  version = "0.6.0";
  src = pkgs.fetchPypi {
    inherit pname version;
    hash = "sha256-J+dzVkIyAE9PgQ/R+FI2Zz7DpW7X8SBvye2GcOvtuXo=";
  };
  '';
in
pkgs.python3Packages.buildPythonPackage {
  inherit pname version src postPatch;
  format = "pyproject";

  nativeBuildInput = with pkgs.python3Packages; [
    setuptools
    setuptools-rust
    wheel
  ];

  cargoDeps = rustPlatform.fetchCargoTarball {
    inherit src postPatch;
    name = "${pname}-${version}";
    hash = "sha256-Q7XO+auj4tKDAGbqNn9pmJg8EJvooN2ie0lWwZVrld4=";
  };

  nativeBuildInputs = [
    rustPlatform.cargoSetupHook
    setuptools-rust
    cargo
    rustc
  ];

  buildInputs = lib.optionals stdenv.isDarwin [ libiconv ];

  propagatedBuildInputs = [
    requests
    regex
    blobfile
  ];

  # almost all tests require network access
  doCheck = false;

  pythonImportsCheck = [
    "tiktoken"
  ];

  meta = with lib; {
    description = "tiktoken is a fast BPE tokeniser for use with OpenAI's models.";
    homepage = "https://github.com/openai/tiktoken";
    license = licenses.mit;
    maintainers = with maintainers; [ happysalada ];
  };
}