{ pkgs }:

pkgs.python3Packages.buildPythonPackage rec {
  pname = "langchain-openai";
  version = "0.1.1";
  pyproject = true;

  src = pkgs.fetchPypi {
    pname = "langchain_openai";
    inherit version;
    hash = "sha256-0Q6an8TI6pnKmPI4CM5Ex9zdZTVKwHrRCv6HTs80Aco=";
  };

  nativeBuildInputs = [
    pkgs.python3Packages.poetry-core
  ];

  propagatedBuildInputs = [
    pkgs.python3Packages.langchain-core
  ];

  # PyPI source does not have tests
  doCheck = false;

  pythonImportsCheck = [
    "langchain_openai"
  ];

  meta = with pkgs.lib; {
    description = "This package contains the LangChain integrations for OpenAI through their openai SDK.";
    homepage = "https://github.com/langchain-ai/langchain";
    license = licenses.mit;
  };
}