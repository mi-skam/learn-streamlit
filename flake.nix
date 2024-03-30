{
  description = "A dev environment for streamlit development";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
   };

  outputs = { self, nixpkgs, flake-utils, ... }@attrs:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
        pythonEnv = pkgs.python3.withPackages (ps:
          with ps;
          [
            # Add Python packages here
            pip
            streamlit
            openai
            langchain
            langchain-openai
            python-dotenv
          ]);
      in {
        devShells.default = pkgs.mkShell {
          buildInputs = [
            pythonEnv
            # Add other build inputs if necessary
          ];
        };
      });
}
