import logging

from .operations import filesystem, git


def install():
    logging.info("Installing vim...")

    filesystem.create_directory_if_not_exists("~/temp")
    filesystem.create_directory_if_not_exists("~/.vim/bundle")

    git.clone_repository_if_not_exists(
        "https://github.com/joseph62/dot-files", "~/temp/dot-files"
    )
    git.clone_repository_if_not_exists(
        "https://github.com/VundleVimVundle.vim.git", "~/.vim/bundle/Vundle.vim"
    )

    filesystem.update_file("~/temp/dot-files/resources/vimrc", "~/.vimrc")

    logging.info("Installed vim.")


if __name__ == "__main__":
    install()
