import sys
import webbrowser
import subprocess


def parse_url(cmdline_output):
    lines = (l.lstrip() for l in cmdline_output.splitlines())
    target_line = next(l for l in lines if l.startswith("Fetch URL"))
    _, url = target_line.split(":", 1)
    url = url.strip()
    return convert_to_browser_url(url)


def convert_to_browser_url(url):
    if url.endswith(".git"):
        url = url[:-4]
    if url.startswith("https:"):
        return url
    if url.startswith("git@"):
        return 'https://' + url[len("git@"):].replace(":", "/")
    return url


def main():
    """Open the home page of remote origin in browser."""
    cmd = ["git", "remote", "show", "origin", "-n"]
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    if p.returncode != 0:
        print(err)
        sys.exit(1)
    url = parse_url(out)
    webbrowser.open(url, autoraise=True)


if __name__ == "__main__":
    main()
