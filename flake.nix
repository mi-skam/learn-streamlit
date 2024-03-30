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
        
      in {
        devShells.default =  (pkgs.buildFHSUserEnv {
          name = "streamlit-env";
          targetPkgs = pkgs: (with pkgs; [
            python312
            python312Packages.pip
            python312Packages.virtualenv
          ]);
        }).env;
      });
}
