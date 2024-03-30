{ lib
, buildPythonPackage
, fetchPypi
, poetry-core
, langchain-core
, lxml
, pythonOlder
}:

buildPythonPackage rec {
  pname = "langchain-text-splitters";
  version = "0.1.1";
  pyproject = true;

  disabled = pythonOlder "3.11";

  src = fetchPypi {
    pname = "langchain-openai";
    inherit version;
    hash = "sha256-rEWfqYeZ9RF61UJakzCyGWEyHjC8GaKi+fdh3a3WKqE=";
  };

  nativeBuildInputs = [
    poetry-core
  ];

  propagatedBuildInputs = [
    langchain-core
  ];

  # PyPI source does not have tests
  doCheck = false;

  pythonImportsCheck = [
    "langchain_openai"
  ];

  meta = with lib; {
    description = "This package contains the LangChain integrations for OpenAI through their openai SDK.";
    homepage = "https://github.com/langchain-ai/langchain";
    license = licenses.mit;
  };
}