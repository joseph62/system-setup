import logging

from .operations import filesystem, git


def install():
    logging.info("Installing zsh...")

    filesystem.create_directory_if_not_exists("~/temp")
    filesystem.create_directory_if_not_exists("~/.local/opt")
    filesystem.create_directory_if_not_exists("~/.local/etc/dot-files")

    git.clone_repository_if_not_exists(
        "https://github.com/joseph62/dot-files", "~/temp/dot-files"
    )
    git.clone_repository_if_not_exists(
        "https://github.com/zsh-users/zsh-syntax-highlighting",
        "~/.local/opt/zsh-sytax-highlighting",
    )

    filesystem.update_file(
        "~/temp/dot-files/resources/aliases", "~/.local/etc/dot-files/.aliases"
    )
    filesystem.update_file(
        "~/temp/dot-files/resources/environment", "~/.local/etc/dot-files/.environment"
    )
    filesystem.update_file("~/temp/dot-files/resources/zshrc", "~/.zshrc")

    logging.info("Installed zsh.")


if __name__ == "__main__":
    install()
