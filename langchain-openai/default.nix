{ pkgs }:

pkgs.python3Packages.buildPythonPackage rec {
  pname = "langchain-openai";
  version = "0.0.8";
  pyproject = true;

  src = pkgs.fetchPypi {
    pname = "langchain_openai";
    inherit version;
    hash = "sha256-t6un/MUjBeeLCBl+vFT8RcwG28QLpbkTvEiiKzCk9ck=";
  };

  nativeBuildInputs = [
    pkgs.python3Packages.poetry-core
  ];

  propagatedBuildInputs = with pkgs.python3Packages; [
    langchain-core
    openai
    tiktoken
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