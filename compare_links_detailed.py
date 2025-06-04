# Compares all Markdown links in readme.md and CHANGELOG.md and displays mismatched links in each file
import re
import os


def extract_links_with_url(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()
    # Remove Table of Contents and only count resource sections
    toc = re.search(r"^##? .+Table of Contents.*$", text, re.IGNORECASE | re.MULTILINE)
    if toc:
        after_toc = text[toc.end() :]
        section = re.search(r"^##? .+", after_toc, re.MULTILINE)
        content = after_toc[section.start() :] if section else after_toc
    else:
        section = re.search(r"^##? .+", text, re.MULTILINE)
        content = text[section.start() :] if section else text
    # Extract all Markdown links: [text](url)
    links = re.findall(r"\[([^\]]+)\]\((https?://[^\)]+)\)", content)
    # Return as dict: url -> text
    return {url.strip(): text.strip() for text, url in links}


def extract_links_from_linkdump(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()
    # Extract all https links from lines like [text](url) (ignore ✅ and comments)
    links = re.findall(r"\[([^\]]+)\]\((https?://[^\)]+)\)", text)
    return {url.strip(): text.strip() for text, url in links}


def print_missing_links(title, missing_urls, link_dict):
    print(f"\n{title}")
    if missing_urls:
        for url in sorted(missing_urls):
            print(f"- [{link_dict[url]}]({url})")
    else:
        print("(None)")


base_dir = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(base_dir, "readme.md")
changelog_path = os.path.join(base_dir, "CHANGELOG.md")
linkdump_path = os.path.join(base_dir, "linkdump.md")

readme_links = extract_links_with_url(readme_path)
changelog_links = extract_links_with_url(changelog_path)
linkdump_links = extract_links_from_linkdump(linkdump_path)

readme_urls = set(readme_links.keys())
changelog_urls = set(changelog_links.keys())
linkdump_urls = set(linkdump_links.keys())

print(
    f"Stats: readme.md={len(readme_urls)}, CHANGELOG.md={len(changelog_urls)}, linkdump.md={len(linkdump_urls)}"
)

missing_in_readme = changelog_urls - readme_urls
missing_in_changelog = readme_urls - changelog_urls

print_missing_links(
    "Links in CHANGELOG.md but not in readme.md (Markdown format):",
    missing_in_readme,
    changelog_links,
)

print_missing_links(
    "Links in readme.md but not in CHANGELOG.md (Markdown format):",
    missing_in_changelog,
    readme_links,
)

# New check: all linkdump links must be present in readme.md
missing_from_readme = linkdump_urls - readme_urls
print_missing_links(
    "Links in linkdump.md but NOT in readme.md (Markdown format):",
    missing_from_readme,
    linkdump_links,
)
