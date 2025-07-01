Changelog
---------

Here you can see the most important changes between each release

0.9.5 (July 1st, 2025)
^^^^^^^^^^^^^^^^^^^^^^

PR #12 by @vsalomaki, including changes from @jarmokortetjarvi

Changes

- The tests are in working order and being run in github-actions, to ease up the update of marshmallow-update task if anyone is up for it.
- Multiple changes from @jarmokortetjarvi s branch
- Rename requests to requestmodels and responses to responsemodels for clarity
- black format applied

Added endpoints

- AccountingLedger.nv
- accountlist.nv
- Accounting.nv
- accountingperiodlist.nv
- GetCustomer.nv (CustomerList)
- GetSalesInvoice.nv
- updatesalesinvoicestatus.nv
- matchcreditnote.nv
- SalesPaymentList.nv
- SalesPayment.nv

0.9.4 (January 12th, 2023)
^^^^^^^^^^^^^^^^^^^^^^^^^^

- Add support for new resources - PR #5 by @tristen-tooming, PR #10 by @jarmokortetjarvi
    - Accounting
        - Create: Accounting.nv
    - Product
        - Create & update: Product.nv
        - List: ProductList.nv
    - Dimension
        - Create: DimensionItem.nv
        - List: DimensionList.nv
    - Purchase Invoice
        - Get: GetPurchaseInvoice.nv
        - List: PurchaseInvoiceList.nv

- Fix package dependencies configuration
- Housekeeping: Code styling with black, import order with isort


0.9.3 (October 7th, 2022)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Fix sales invoice schema for `invoicing_customer_country_code`


0.9.2 (February 5th, 2021)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- PR #6: Fixed accounting dimension's Item None value error - @kiuru
- PR #7: Sales invoices: invoice status to attributed version - @ajmyyra


0.9.1 (January 28th, 2020)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- PR #4: Added VAT code and voucher line NetvisorKey for accounting model - @kiuru


0.9.0 (October 2nd, 2019)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Breaking change in SalesInvoiceAttachmentLineSchema: the document data and type have own fields now instead of using hacky concatenated string
- Fix schema parsing to work with never versions of deps (tested with marshmallow 2.20.4 and xmltodict 0.12.0, upgrading to marshmallow 3.x.x pending)


0.8.7 (September 12th, 2019)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Customer schema: add default reference, default text before / after invoice lines support


0.8.6 (August 16th, 2019)
^^^^^^^^^^^^^^^^^^^^^^^^^
- PR #3: Value date and currency for invoices, invoice print format for customers - @ajmyyra


0.8.5 (June 26th, 2019)
^^^^^^^^^^^^^^^^^^^^^^^
- PR #1: Typo fix in sales invoice number and version bump - @ajmyyra


0.8.0 (February 7th, 2019)
^^^^^^^^^^^^^^^^^^^^^^^^^^
- Added support for Invoice attachments



0.7.0 (September 19th, 2016)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Added support for getting accounting data.

0.6.0 (August 16th, 2016)
^^^^^^^^^^^^^^^^^^^^^^^^^

- Fixed compatibility with the latest version of xmltodict. Netvisor.py now
  requires xmltodict >= 0.10.1.
- Added support for customer's email invoicing address.
- Fixed case problem with product's unit price type.
- Added official Python 3.5 support.

0.5.0 (November 5th, 2015)
^^^^^^^^^^^^^^^^^^^^^^^^^^

- Added support for invoice line free text field when creating a sales invoice.

0.4.0 (September 28th, 2015)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Updated Marshmallow requirement to >= 2.0.0.
- Added support for additional address line when creating/updating a customer.

0.3.4 (September 10th, 2015)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Fixed UnicodeEncodeError when making a request containing non-ASCII
  characters.

0.3.3 (May 29th, 2015)
^^^^^^^^^^^^^^^^^^^^^^

- Fixed too strict validation for payment term fields returned by Netvisor API
  in ``netvisor.sales_invoices.get()``.

0.3.2 (April 30th, 2015)
^^^^^^^^^^^^^^^^^^^^^^^^

- Fixed ``netvisor.sales_invoices.get()`` crashing when the
  ``<SalesInvoiceAmount>`` element had attributes in the XML response.
- Fixed ``netvisor.sales_invoices.get()`` crashing when any of the following
  elements were empty in the XML response:

  - seller identifier
  - invoicing customer address line
  - invoicing customer post number
  - invoicing customer town
  - delivery address name
  - delivery address line
  - delivery address post number
  - delivery address town
  - delivery address country code
  - accounting account suggestion

- Fixed ``netvisor.sales_invoices.list()`` crashing when customer code was empty
  in the XML response.
- Fixed ``netvisor.sales_invoices.list()`` crashing when invoice status had no
  substatus in the XML response.

0.3.1 (April 29th, 2015)
^^^^^^^^^^^^^^^^^^^^^^^^

- Fixed ``netvisor.schemas`` package missing from the source distribution.

0.3.0 (April 29th, 2015)
^^^^^^^^^^^^^^^^^^^^^^^^

- Added official Python 3.4 support.
- Added creating and updating of customers and sales invoices.
- Changed response parsing not to rename and restructure the responses to keep
  the Python API implementation simpler and more consistent with the Netvisor
  API's XML responses.
- Changed response parsing to use Marshmallow.
- Changed ``Request`` to take ``params`` as a single keyword argument instead of
  as named variable-length arguments.
- Fixed tests to work with responses 0.3.0.

0.2.0 (April 8th, 2014)
^^^^^^^^^^^^^^^^^^^^^^^

- Added support for InvoiceNumber and InvoicesAboveNetvisorKey parameters to
  sales invoice listing.
- Changed xmltodict's dict constructor from ``OrderedDict`` to to ``dict``.
- Fixed parsing of sales invoice with multiple lines.

0.1.0 (March 26th, 2014)
^^^^^^^^^^^^^^^^^^^^^^^^

- Initial public release.
