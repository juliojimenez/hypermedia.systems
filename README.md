# hypermedia.systems

Following along with the examples from the book [Hypermedia Systems](https://hypermedia.systems).

The code here is slightly different from the book, as I try to use types where I can, and check for them using [Mypy](https://mypy.readthedocs.io/en/stable/index.html), a static type checker for Python.

## Running an Example

Clone the repo...
```bash
git clone https://github.com/juliojimenez/hypermedia.systems
```
Go to an example...
```bash
cd chapter-3/1-simple-hello-world/
```
And run it...
```bash
pip3 install -r requirements.txt
python3 app.py
```
You can also explore the project by using the links below.

## Examples

### Chapter 3

- [Simple Hello World](./chapter-3/1-simple-hello-world/)
- [Simple Hello World to a Redirect](./chapter-3/2-simple-hello-world-to-a-redirect/)
- [Showing a Searchable List of Contacts](./chapter-3/3-showing-a-searchable-list-of-contacts/)
- [Adding a New Contact](./chapter-3/4-adding-a-new-contact/)
- [Viewing the Details of a Contact](./chapter-3/5-viewing-the-details-of-a-contact/)
- [Editing a Contact](./chapter-3/6-editing-a-contact/)
- [Deleting a Contact](./chapter-3/7-deleting-a-contact/)

### Chapter 4

- [Installing HTMX as a Third Party Dependency](./chapter-4/1-installing-htmx-third-party/)
- [Triggering HTTP Requests](./chapter-4/2-triggering-http-requests/)
- [HTMX vs. Plain HTML Responses](./chapter-4/3-htmx-vs-plain-html-responses/)
- [Targeting Other Elements](./chapter-4/4-targeting-other-elements/)
- [Swap Styles](./chapter-4/5-swap-styles/)
- Using Events
    - [mouseenter](./chapter-4/6-using-events-mouseenter/)
    - [click and keyup](./chapter-4/7-using-events-click-and-keyup/)
- Passing Request Parameters
    - [Enclosing Forms](./chapter-4/8-passing-request-parameters-enclosing-forms/)
    - [Including Inputs](./chapter-4/9-passing-request-parameters-including-inputs/)
    - [Inline Values](./chapter-4/10-passing-request-parameters-inline-values/)
- [History Support](./chapter-4/11-history-support/)

### Chapter 5

- [Installing HTMX as a Vendored Dependency](./chapter-5/1-installing-htmx-vendored/)
- [Adding hx-boost to Contact.app](./chapter-5/2-adding-hx-boost-to-contact-app/)

## Support

Python 3.11+