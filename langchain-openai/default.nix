{ pkgs
, _tiktoken
}:

pkgs.python3Packages.buildPythonPackage rec {
  pname = "langchain-openai";
  version = "0.1.1";
  pyproject = true;

  src = pkgs.fetchPypi {
    pname = "langchain_openai";
    inherit version;
    hash = "sha256-MDdGY3qXGx8yB4r7Xpe5BPqU05f7s7bB9x1qX07cbuQ=";
  };

  nativeBuildInputs = [
    pkgs.python3Packages.poetry-core
  ];

  propagatedBuildInputs = with pkgs.python3Packages; [
    langchain-core
    openai
    _tiktoken
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