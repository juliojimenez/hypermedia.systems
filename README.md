# hypermedia.systems

[![Type Checker](https://github.com/juliojimenez/hypermedia.systems/actions/workflows/typechecker.yml/badge.svg)](https://github.com/juliojimenez/hypermedia.systems/actions/workflows/typechecker.yml) [![Tests](https://github.com/juliojimenez/hypermedia.systems/actions/workflows/tests.yml/badge.svg)](https://github.com/juliojimenez/hypermedia.systems/actions/workflows/tests.yml)

Examples from the book [Hypermedia Systems](https://hypermedia.systems).

The code here is slightly different from the book, as I try to use types where I can, and check for them using [Mypy](https://mypy.readthedocs.io/en/stable/index.html), a static type checker for Python. 

[PyTest](https://docs.pytest.org/en/7.4.x/) is used for testing. While inside an example directory simply run `pytest` to run the tests for that example.

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

Each example runs on a different port. Run multiple examples simultaneously and compare them in the browser!

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
- [Adding hx-boost to Contacts.app](./chapter-5/2-adding-hx-boost-to-contact-app/)
- [A Second Step: Deleting Contacts With HTTP DELETE](./chapter-5/3-a-second-step-deleting-contacts-with-http-delete/)
- Next Steps: Validating Contact Emails
    - [Update Our Input Type](./chapter-5/4-next-steps-validating-contact-emails-update-our-input-type/)
    - [Inline Validation](./chapter-5/5-next-steps-validating-contact-emails-inline-validation/)
    - [Validating Emails Server-Side](./chapter-5/6-next-steps-validating-contact-emails-validating-emails-server-side/)
    - [Taking The User Experience Further](./chapter-5/7-next-steps-validating-contact-emails-taking-the-user-experience-further/)
    - [Debouncing Our Validation Requests](./chapter-5/8-next-steps-validating-contact-emails-debouncing-our-validation-requests/)
    - [Ignoring Non-Mutating Keys](./chapter-5/9-next-steps-validating-contact-emails-ignoring-non-mutating-keys/)
- Another Application Improvement: Paging
    - [Adding Paging Widgets](./chapter-5/10-another-application-improvement-paging-adding-paging-widgets/)
    - [Click To Load](./chapter-5/11-another-application-improvement-paging-click-to-load/)
    - [Infinite Scroll](./chapter-5/12-another-application-improvement-paging-infinite-scroll/)

### Chapter 6

- [Adding Active Search](./chapter-6/1-adding-active-search/)
    - [Targeting The Correct Element](./chapter-6/2-targeting-the-correct-element/)
    - [Paring Down Our Content](./chapter-6/3-paring-down-our-content/)  
    - [HTTP Headers In HTMX](./chapter-6/4-http-headers-in-htmx/)
    - [Factoring Your Templates](./chapter-6/4-http-headers-in-htmx/)
    - [Using Our New Template](./chapter-6/4-http-headers-in-htmx/)
    - [Updating The Navigation Bar With "hx-push-url"](./chapter-6/5-updating-the-navigation-bar-with-hx-push-url/)
    - [Adding A Request Indicator](./chapter-6/6-adding-a-request-indicator/)
- [Lazy Loading](./chapter-6/7-lazy-loading/) 
    - [Pulling Out The Expensive Code](./chapter-6/8-pulling-out-the-expensive-code/)
    - [Adding An Indicator](./chapter-6/9-adding-an-indicator/)
    - [But That's Not Lazy!](./chapter-6/10-but-thats-not-lazy/)
- [Inline Delete](./chapter-6/11-inline-delete/)
    - [Narrowing Our Target](./chapter-6/12-narrowing-our-target/) 
    - [Updating The Server Side](./chapter-6/13-updating-the-server-side/)
    - [Taking Advantage of "htmx-swapping"](./chapter-6/14-taking-advantage-of-htmx-swapping/)
- [Bulk Delete](./chapter-6/15-bulk-delete/) <span style="background-color:red;padding:1px 5px;font-weight:bolder;border-radius:2px;">New</span>

## Support

Python 3.11+

## Dependencies

- [HTMX v1.9.5](https://htmx.org)
- [missing.css v1.0.10](https://missing.style)
    - Not sure what's going on with the package hosting for this, but I had to grab the artifact from the latest tag in the [repo](https://github.com/bigskysoftware/missing).
    - It was working fine when I started this repository. If it starts working again, please submit an issue or hit me up on [X](https://twitter.com/LispDev).