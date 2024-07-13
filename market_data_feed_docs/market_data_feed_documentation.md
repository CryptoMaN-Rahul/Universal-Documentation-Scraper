# Market Data Feed Documentation

## [API Documentation – Fast Secure Free – Upstox | Upstox Developer API](https://upstox.com/developer/api-documentation#docusaurus_skipToContent_fallback)

![Upstox API zero brokerage](/developer/api-documentation/assets/images/brokerage_free_banner-b1a30a11856232fd221b6abff1c53799.webp)

[\* Terms and Conditions](https://marketing-creative-and-docs.s3.ap-south-1.amazonaws.com/API_T%26C/T%26C+apply.pdf)

# Upstox API Documentation

The Upstox API comprises a suite of RESTful APIs designed to supply the necessary data for constructing a comprehensive investment and trading platform. These APIs enable real-time order execution, user portfolio management, live market data streaming via Websockets, and more, all presented in an easily comprehensible API collection.

All requests are transmitted securely via HTTPS, and they are formatted with the 'application/json' content type. All responses are provided in JSON format, except for the instrumental API, which yields a CSV response..

To utilize these APIs, creating an application within the Developer Console is imperative, generating both an apiKey and apiSecret.You need to specify a redirect URL, which will be invoked following the login process with the auth code. Optionally, you can provide a Postback URL where you can receive live updates on order statuses.

For traders, the creation of apps can be accomplished directly from the Upstox mobile app or the desktop platform, accessible from the Apps section within the Account Tab. Head over to [create an app](https://account.upstox.com/developer/apps). For businesses interested in integrating Upstox APIs, you can [contact us](https://upstox.com/uplink/business-trading-api/), and we will expedite the development of a customized app to meet your specific needs.

It is strongly advised against embedding the apiSecret within your frontend application. Instead, it is recommended to establish a remote backend system responsible for managing the handshake process on behalf of the frontend app. Inadvertently disclosing the apiSecret within the frontend application could render your app susceptible to security threats and potential issues.

We also boast a thriving [Upstox developer community](https://community.upstox.com/c/developer-api/15) that you can tap into to connect with like-minded Upstox API users. Here, you can inquire about API-related questions and engage with the community members.

---

## [API Documentation – Fast Secure Free – Upstox | Upstox Developer API](https://upstox.com/developer/api-documentation/)

![Upstox API zero brokerage](/developer/api-documentation/assets/images/brokerage_free_banner-b1a30a11856232fd221b6abff1c53799.webp)

[\* Terms and Conditions](https://marketing-creative-and-docs.s3.ap-south-1.amazonaws.com/API_T%26C/T%26C+apply.pdf)

# Upstox API Documentation

The Upstox API comprises a suite of RESTful APIs designed to supply the necessary data for constructing a comprehensive investment and trading platform. These APIs enable real-time order execution, user portfolio management, live market data streaming via Websockets, and more, all presented in an easily comprehensible API collection.

All requests are transmitted securely via HTTPS, and they are formatted with the 'application/json' content type. All responses are provided in JSON format, except for the instrumental API, which yields a CSV response..

To utilize these APIs, creating an application within the Developer Console is imperative, generating both an apiKey and apiSecret.You need to specify a redirect URL, which will be invoked following the login process with the auth code. Optionally, you can provide a Postback URL where you can receive live updates on order statuses.

For traders, the creation of apps can be accomplished directly from the Upstox mobile app or the desktop platform, accessible from the Apps section within the Account Tab. Head over to [create an app](https://account.upstox.com/developer/apps). For businesses interested in integrating Upstox APIs, you can [contact us](https://upstox.com/uplink/business-trading-api/), and we will expedite the development of a customized app to meet your specific needs.

It is strongly advised against embedding the apiSecret within your frontend application. Instead, it is recommended to establish a remote backend system responsible for managing the handshake process on behalf of the frontend app. Inadvertently disclosing the apiSecret within the frontend application could render your app susceptible to security threats and potential issues.

We also boast a thriving [Upstox developer community](https://community.upstox.com/c/developer-api/15) that you can tap into to connect with like-minded Upstox API users. Here, you can inquire about API-related questions and engage with the community members.

---

## [Developer API | Upstox Developer API](https://upstox.com/developer/api-documentation/open-api)

- [](/developer/api-documentation/)
- Developer API

# Developer API

Develop your app on the Upstox platform, utilizing a robust collection of REST APIs that deliver the necessary data for building a comprehensive investment and trading platform. With this API set, you can execute real-time orders, effectively manage user portfolios, stream live market data via Websockets, and more, all in a user-friendly and easily comprehensible manner.

## [description AuthenticationUser authentication and authorization flow.](/developer/api-documentation/authentication)## [folder API Structure3 items](/developer/api-documentation/request-response)## [description Rate LimitsAPI rate limits.](/developer/api-documentation/rate-limiting)## [folder SDK2 items](/developer/api-documentation/sdk)## [description InstrumentsGet BOD instruments.](/developer/api-documentation/instruments)## [folder Login3 items](/developer/api-documentation/login)## [folder User2 items](/developer/api-documentation/user)## [folder Charges1 items](/developer/api-documentation/charges)## [folder Orders9 items](/developer/api-documentation/orders)## [folder Portfolio3 items](/developer/api-documentation/portfolio)## [folder Trade Profit And Loss3 items](/developer/api-documentation/trade-profit-and-loss)## [folder Historical Data2 items](/developer/api-documentation/historical-data)## [folder Market Quote3 items](/developer/api-documentation/market-quote)## [folder Market Information3 items](/developer/api-documentation/market-information)## [folder Option Chain2 items](/developer/api-documentation/option-chain)## [folder Websocket4 items](/developer/api-documentation/websocket)## [folder Websocket implementation1 items](/developer/api-documentation/websocket-implementation)## [description WebhookWebhook for real-time order updates.](/developer/api-documentation/webhook)## [folder Appendix9 items](/developer/api-documentation/appendix)[NextAuthentication](/developer/api-documentation/authentication)

---

## [Uplink Business | Upstox Developer API](https://upstox.com/developer/api-documentation/uplink-business/introduction)

- [](/developer/api-documentation/)
- UpLink Business

# Uplink Business

UpLink Business is the middleware that helps all multi-clients to place orders through Upstox’s platform complying with the latest SEBI norms.

New to UpLink Business?

- To use UpLink Business, you would need a multi-client API which is created on-demand for our business partners.
- To request for a multi-client API, you can either [fill the form](https://upstox.com/uplink/business-trading-api/) on UpLink Business webpage or create a thread on [Upstox Community](https://community.upstox.com/).

## [description Place OrderPlace an order with all possible combinations.](/developer/api-documentation/uplink-business/docs/place-order)## [description Modify OrderModify pending or open orders.](/developer/api-documentation/uplink-business/docs/modify-order)## [description Cancel OrderCancel pending or open orders.](/developer/api-documentation/uplink-business/docs/cancel-order)## [description CDSL AuthCDSL authorization steps for delivery sale transactions.](/developer/api-documentation/uplink-business/docs/cdsl-auth)

NOTE

- When dealing with a multi-client application, the process of placing, canceling, or modifying orders necessitates the use of the Uplink Business approach. This method involves utilizing an HTML form containing order details, which is then submitted to the Uplink UI. The subsequent order processing tasks are efficiently managed by the Uplink UI.
- It's important to note that employing the order API for order placement is not permissible with a multi-client app. Attempting to do so will trigger an error message stating, ""Access to this API has been restricted for your account. Please use 'Uplink Business' to place/modify/cancel the order."

[NextPlace Order](/developer/api-documentation/uplink-business/docs/place-order)

---

## [Example Code | Upstox Developer API](https://upstox.com/developer/api-documentation/example-code/introduction)

- [](/developer/api-documentation/)
- Example Code

# Example Code

## [folder Login2 items](/developer/api-documentation/example-code/login/get-token)## [folder User2 items](/developer/api-documentation/example-code/user/get-profile)## [folder Charges1 items](/developer/api-documentation/example-code/charges/brokerage-details)## [folder Order9 items](/developer/api-documentation/example-code/orders/place-order)## [folder Portfolio3 items](/developer/api-documentation/example-code/portfolio/convert-positions)## [folder Trade Profit and Loss3 items](/developer/api-documentation/example-code/trade-profit-and-loss/get-report-meta-data)## [folder Historical Data2 items](/developer/api-documentation/example-code/historical-data/historical-candle-data)## [folder Market Quote3 items](/developer/api-documentation/example-code/market-quote/full-market-quotes)## [folder Market Information3 items](/developer/api-documentation/example-code/market-information/market-holidays)## [folder Option Chain2 items](/developer/api-documentation/example-code/option-chain/option-contracts)

[NextGet Token](/developer/api-documentation/example-code/login/get-token)

---

## [Announcements | Upstox Developer API](https://upstox.com/developer/api-documentation/announcements)

On this page

# Announcements

This section is dedicated to providing you with the most recent updates and essential information.

## Active Announcements​

- **Apr 25, 2024: CSV Instruments File Deprecation Notice**  
  The [CSV format](/developer/api-documentation/instruments#csv-files) for the instruments file will soon be deprecated. We recommend users to transition to the [JSON version](/developer/api-documentation/instruments#json-files) for improved functionality and support.  
  [Read more](/developer/api-documentation/announcements/instruments-csv-deprecation-notice)

- **Mar 7, 2024: New URL and Simplified Headers**  
  Upstox API now accessible at a new URL <https://api.upstox.com/v2> with simplified header requirements. Old and new URLs operational during transition. Migration advised.  
  [Read more](/developer/api-documentation/announcements/new-url-and-simplified-headers)

Remember to check back regularly for the latest news and updates.

- Active Announcements

---

## [API Documentation – Fast Secure Free – Upstox | Upstox Developer API](https://upstox.com/developer/api-documentation/#docusaurus_skipToContent_fallback)

![Upstox API zero brokerage](/developer/api-documentation/assets/images/brokerage_free_banner-b1a30a11856232fd221b6abff1c53799.webp)

[\* Terms and Conditions](https://marketing-creative-and-docs.s3.ap-south-1.amazonaws.com/API_T%26C/T%26C+apply.pdf)

# Upstox API Documentation

The Upstox API comprises a suite of RESTful APIs designed to supply the necessary data for constructing a comprehensive investment and trading platform. These APIs enable real-time order execution, user portfolio management, live market data streaming via Websockets, and more, all presented in an easily comprehensible API collection.

All requests are transmitted securely via HTTPS, and they are formatted with the 'application/json' content type. All responses are provided in JSON format, except for the instrumental API, which yields a CSV response..

To utilize these APIs, creating an application within the Developer Console is imperative, generating both an apiKey and apiSecret.You need to specify a redirect URL, which will be invoked following the login process with the auth code. Optionally, you can provide a Postback URL where you can receive live updates on order statuses.

For traders, the creation of apps can be accomplished directly from the Upstox mobile app or the desktop platform, accessible from the Apps section within the Account Tab. Head over to [create an app](https://account.upstox.com/developer/apps). For businesses interested in integrating Upstox APIs, you can [contact us](https://upstox.com/uplink/business-trading-api/), and we will expedite the development of a customized app to meet your specific needs.

It is strongly advised against embedding the apiSecret within your frontend application. Instead, it is recommended to establish a remote backend system responsible for managing the handshake process on behalf of the frontend app. Inadvertently disclosing the apiSecret within the frontend application could render your app susceptible to security threats and potential issues.

We also boast a thriving [Upstox developer community](https://community.upstox.com/c/developer-api/15) that you can tap into to connect with like-minded Upstox API users. Here, you can inquire about API-related questions and engage with the community members.

---

## [Developer API | Upstox Developer API](https://upstox.com/developer/api-documentation/open-api#docusaurus_skipToContent_fallback)

- [](/developer/api-documentation/)
- Developer API

# Developer API

Develop your app on the Upstox platform, utilizing a robust collection of REST APIs that deliver the necessary data for building a comprehensive investment and trading platform. With this API set, you can execute real-time orders, effectively manage user portfolios, stream live market data via Websockets, and more, all in a user-friendly and easily comprehensible manner.

## [description AuthenticationUser authentication and authorization flow.](/developer/api-documentation/authentication)## [folder API Structure3 items](/developer/api-documentation/request-response)## [description Rate LimitsAPI rate limits.](/developer/api-documentation/rate-limiting)## [folder SDK2 items](/developer/api-documentation/sdk)## [description InstrumentsGet BOD instruments.](/developer/api-documentation/instruments)## [folder Login3 items](/developer/api-documentation/login)## [folder User2 items](/developer/api-documentation/user)## [folder Charges1 items](/developer/api-documentation/charges)## [folder Orders9 items](/developer/api-documentation/orders)## [folder Portfolio3 items](/developer/api-documentation/portfolio)## [folder Trade Profit And Loss3 items](/developer/api-documentation/trade-profit-and-loss)## [folder Historical Data2 items](/developer/api-documentation/historical-data)## [folder Market Quote3 items](/developer/api-documentation/market-quote)## [folder Market Information3 items](/developer/api-documentation/market-information)## [folder Option Chain2 items](/developer/api-documentation/option-chain)## [folder Websocket4 items](/developer/api-documentation/websocket)## [folder Websocket implementation1 items](/developer/api-documentation/websocket-implementation)## [description WebhookWebhook for real-time order updates.](/developer/api-documentation/webhook)## [folder Appendix9 items](/developer/api-documentation/appendix)[NextAuthentication](/developer/api-documentation/authentication)

---

## [Authentication | Upstox Developer API](https://upstox.com/developer/api-documentation/authentication)

- [](/developer/api-documentation/)
- [Developer API](/developer/api-documentation/open-api)
- Authentication

On this page

# Authentication

![Login flow](/developer/api-documentation/assets/images/loginflow-58e94762548c9142d35fe1d479df21bf.webp#block)

Upstox uses standard OAuth 2.0 for customer authentication and login.

All logins are handled by upstox.com. There is no public endpoint for other applications to directly log the customer into their upstox.com. For security and compliance purposes, all logins and logouts are handled exclusively by upstox.com.

## Perform Authentication​

The login window is a web page hosted at the following link.

Your client application must trigger the opening of the above URL using Webview (or similar technology) and pass the following parameters:

| Parameter     | Description                                                                                                                             |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| client_id     | The API key obtained during the app generation process.                                                                                 |
| redirect_uri  | The URL to which the user will be redirected post authentication; must match the URL provided during app generation.                    |
| state         | An optional parameter. If specified, will be returned after authentication, allowing for state continuity between request and callback. |
| response_type | This value must always be .                                                                                                             |

URL construction:

Sample URL:

NOTE

In OAuth, client_id means API Key (not customer UCC) and client_secret means API Secret.

NOTE

If you encounter an error, it likely stems from inconsistencies in the request parameters (, , and ) compared to the information registered during app creation. Ensure you verify these parameters and correct any discrepancies before making another attempt.

The user will be redirected to the default login page where they will be able to log in.

![Login page](/developer/api-documentation/assets/images/loginpage-bd1c2065c2c8d2c720f0ed703dd48131.webp#block)

NOTE

You also have the option to select [TOTP (Time-based One-Time Password)](https://en.wikipedia.org/wiki/Time-based_one-time_password) as a more secure method for 2FA, compared to the usual SMS OTP, for a safer login. Learn more about activating TOTP on your Upstox account [here](https://help.upstox.com/support/solutions/articles/260346-what-is-totp-and-how-to-enable-totp-for-my-account-from-upstox-web-platform-).

## Receive Auth Code​

Upon successful authentication, this API will redirect to the URL specified in the parameter, with the essential for the token generation included within the request parameters.

| Name  | Description                                                                     |
| ----- | ------------------------------------------------------------------------------- |
| code  | Utilize this code to generate the as part of the next step.                     |
| state | Provided optionally if it was initially included in the request URL parameters. |

## Generate Access Token​

Once the user has authenticated with us, they will be redirected to your redirect URL with an authorization code. The parameter will come as (query parameter).

NOTE

The authorization code is valid for a single use, regardless of whether the access token generation succeeds or encounters an issue.

The last step is to make a server-to-server call between your backend server and Upstox to get an using the authorization code. This can be done by calling the following service:

You will need to pass the following parameters:

| Parameter     | Description                                                                                                                                                   |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| code          | The is a unique parameter included in the URL upon a successful [Authorize API](/developer/api-documentation/authorize) authentication.                       |
| client_id     | The API key obtained during the app generation process.                                                                                                       |
| client_secret | The API secret obtained during the app generation process. This private key remains confidential, known only to the application and the authorization server. |
| redirect_uri  | The URL provided during app generation.                                                                                                                       |
| grant_type    | This value must always be .                                                                                                                                   |

URL construction:

Finally this will return an access token for you. This access token can be successfully passed back to your front-end application to access the Upstox API.

## Extended Token​

Upstox APIs now support the generation of an extended token in addition to the standard access token.

An extended token is designed for long-term use, primarily for read-only API calls. It remains valid for one year from the date it is generated, or until the user revokes access to their account from pro.upstox.com, whichever occurs first. This token allows access to specific user trade data. Below is a list of APIs that can be utilized with the extended token:

#### Supported APIs​

- [Get Positions](/developer/api-documentation/get-positions)
- [Get Holdings](/developer/api-documentation/get-holdings)
- [Get Order Details](/developer/api-documentation/get-order-details)
- [Get Order History](/developer/api-documentation/get-order-history)
- [Get Order Book](/developer/api-documentation/get-order-book)

Enroll for Extended Token

Extended tokens are available for multi-client applications upon request. If your app requires an extended token, please reach out to our support team for enrollment and further assistance.

[PreviousDeveloper API](/developer/api-documentation/open-api)[NextAPI Structure](/developer/api-documentation/request-response)

- Perform Authentication
- Receive Auth Code
- Generate Access Token
- Extended Token

---

## [API Structure | Upstox Developer API](https://upstox.com/developer/api-documentation/request-response)

- [](/developer/api-documentation/)
- [Developer API](/developer/api-documentation/open-api)
- API Structure

# API Structure

## [description Request StructureOverview of the request structure.](/developer/api-documentation/request-structure)## [description Response StructureOverview of the response structure.](/developer/api-documentation/response-structure)## [description Error CodesDescription of the error codes.](/developer/api-documentation/error-codes)

[PreviousAuthentication](/developer/api-documentation/authentication)[NextRequest Structure](/developer/api-documentation/request-structure)

---

## [Rate Limits | Upstox Developer API](https://upstox.com/developer/api-documentation/rate-limiting)

- [](/developer/api-documentation/)
- [Developer API](/developer/api-documentation/open-api)
- Rate Limits

# Rate Limits

In our pursuit of offering a consistent and reliable service, we've established rate limits for our API interactions. These constraints, detailed below, are designed to prevent system overloads and ensure equitable access to all our users. The rate limits are enforced on a per-API, per-user basis.

| Time duration  | Request limit |
| -------------- | ------------- |
| Per second     | 25 requests   |
| Per minute     | 250 requests  |
| Per 30 minutes | 1000 requests |

NOTE

Please adhere to these limits to avoid potential disruptions in service. Exceeding these limits might result in temporary suspension of access.

[PreviousError Codes](/developer/api-documentation/error-codes)[NextSDK](/developer/api-documentation/sdk)

---

## [SDK | Upstox Developer API](https://upstox.com/developer/api-documentation/sdk)

- [](/developer/api-documentation/)
- [Developer API](/developer/api-documentation/open-api)
- SDK

# SDK

## [description Upstox GeneratedGet started with Upstox generated SDK for Python, PHP, NodeJS, Java and .NET](/developer/api-documentation/upstox-generated-sdk)## [description Self GeneratedGenerate SDK in your preferred language.](/developer/api-documentation/self-generated-sdk)

[PreviousRate Limits](/developer/api-documentation/rate-limiting)[NextUpstox Generated](/developer/api-documentation/upstox-generated-sdk)

---

## [Instruments | Upstox Developer API](https://upstox.com/developer/api-documentation/instruments)

- [](/developer/api-documentation/)
- [Developer API](/developer/api-documentation/open-api)
- Instruments

On this page

# Instruments

Note

- **The CSV format for instruments files is being deprecated.** Switch to the JSON format for improved performance. Details at [CSV Instruments File Deprecation Notice](/developer/api-documentation/announcements/instruments-csv-deprecation-notice).
- The list of suspended instruments is available in the [JSON section](/developer/api-documentation/instruments#json-files) below.

Recommendations

- Use for uniquely identifying instruments, as it remains unique for each instrument. Conversely, may be reused by the exchange for a different instrument after its expiry.
- Use Instruments data in JSON format instead of CSV, as its structure has been designed for enhanced robustness and future scalability, making programmatic processing easier.

## CSV Files​

These URLs provide access to the complete list of BOD contracts available for trading on Upstox in CSV format.

- [Complete](https://assets.upstox.com/market-quote/instruments/exchange/complete.csv.gz)
- [NSE](https://assets.upstox.com/market-quote/instruments/exchange/NSE.csv.gz)
- [BSE](https://assets.upstox.com/market-quote/instruments/exchange/BSE.csv.gz)
- [MCX](https://assets.upstox.com/market-quote/instruments/exchange/MCX.csv.gz)

### Sample CSV Record​

| instrument_key | exchange_token | tradingsymbol | name                | last_price              | expiry | strike     | tick_size | lot_size | instrument_type | option_type | exchange |
| -------------- | -------------- | ------------- | ------------------- | ----------------------- | ------ | ---------- | --------- | -------- | --------------- | ----------- | -------- | ------ |
| NSE_FO         | 164693         | 164693        | RELIANCE24JAN1840CE | RELIANCE INDUSTRIES LTD | 424.8  | 2024-01-25 | 1840.0    | 0.05     | 250             | OPTSTK      | CE       | NSE_FO |

### Field Description​

| Name            | Type   | Description                                                                                                                                                                                                                                                          |
| --------------- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| instrument_key  | string | The unique identifier used across Upstox APIs for instrument identification. For the regex pattern applicable to this field, see the [Field Pattern Appendix](/developer/api-documentation/appendix/field-pattern).                                                  |
| exchange_token  | number | The numerical identifier issued by the exchange representing the instrument.                                                                                                                                                                                         |
| tradingsymbol   | string | Shows the trading symbol which could be a combination of symbol name, instrument, expiry date etc. The format of this value may vary between weekly and monthly contracts, leading to inconsistencies. These inconsistencies have been resolved in the JSON version. |
| name            | string | Name of the company (for equity instruments).                                                                                                                                                                                                                        |
| last_price      | number | Last traded price.                                                                                                                                                                                                                                                   |
| expiry          | string | Expiry date (for derivatives). Data format is                                                                                                                                                                                                                        |
| strike          | number | Indicates the predetermined price at which an option can be bought or sold when it's exercised.                                                                                                                                                                      |
| tick_size       | number | Measure of the minimum upward or downward movement in the price of an instrument.                                                                                                                                                                                    |
| lot_size        | number | Minimum size in which the stock futures or index futures can be traded.                                                                                                                                                                                              |
| instrument_type | string | Instrument type of a particular contract.                                                                                                                                                                                                                            |

Possible values: , , etc.  
option_type| string| Option type of the option contracts (applicable only for options contract).  
Possible values: ,  
exchange| string| Exchange to which the order is associated.  
Possible values: , , , , , etc.

## JSON files​

These URLs provide access to the complete list of BOD contracts available for trading on Upstox in JSON format.

- [Complete](https://assets.upstox.com/market-quote/instruments/exchange/complete.json.gz)
- [NSE](https://assets.upstox.com/market-quote/instruments/exchange/NSE.json.gz)
- [BSE](https://assets.upstox.com/market-quote/instruments/exchange/BSE.json.gz)
- [MCX](https://assets.upstox.com/market-quote/instruments/exchange/MCX.json.gz)
- [Suspended](https://assets.upstox.com/market-quote/instruments/exchange/suspended-instrument.json.gz)

### Sample JSON Object​

- EQ
- Futures
- Options
- INDEX

Note

- When you're searching for instrument keys within an instrument JSON file, you can employ the and parameters to refine and narrow down the list of instrument keys. For instance, if you're looking for the instrument key for Reliance Equity, specify the as and the as , excluding other segments and instrument types from your search criteria.

### Field Description

| Field Name | Type   | Description                                    |
| ---------- | ------ | ---------------------------------------------- |
| segment    | string | Segment to which the instrument is associated. |

Possible values: , , , , , , , ,  
name| string| The name of the equity.  
exchange| string| Exchange to which the instrument is associated.  
Possible values: , ,  
isin| string| The International Securities Identification Number.  
instrument_type| string| The instrument types for NSE are present at [NSE India](https://www.nseindia.com/market-data/legend-of-series) and for BSE are present at [BSE India](https://www.bseindia.com/markets/equity/EQReports/tra_trading.aspx).  
instrument_key| string| The unique identifier used across Upstox APIs for instrument identification. For the regex pattern applicable to this field, see the [Field Pattern Appendix](/developer/api-documentation/appendix/field-pattern).  
lot_size| number| The size of one lot of the equity.  
freeze_quantity| number| The maximum quantity that can be frozen.  
exchange_token| string| The exchange-specific token for the equity.  
tick_size| number| The minimum price movement of the equity.  
trading_symbol| string| Trading symbol of the instrument.  
short_name| string| A shorter or abbreviated name of the equity.  
security_type| string| Identifies the classification or status of a security within the market. Valid security types can be found in the [Security Type Appendix](/developer/api-documentation/appendix/equity-security-type)

Note

- When you're searching for instrument keys within an instrument JSON file, you can employ the and parameters to refine and narrow down the list of instrument keys. For instance, if you're looking for the instrument key for Reliance Future, specify the as and the as , excluding other segments and instrument types from your search criteria.

### Field Description

| Field Name        | Type    | Description                                                                                                                                                                                                         |
| ----------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| weekly            | boolean | Indicates if the future is weekly.                                                                                                                                                                                  |
| segment           | string  | Segment to which the instrument is associated. Possible values: , , , , , , , ,                                                                                                                                     |
| name              | string  | The name of the future.                                                                                                                                                                                             |
| exchange          | string  | Exchange to which the instrument is associated. Possible values: , ,                                                                                                                                                |
| expiry            | date    | The expiry date of the future.                                                                                                                                                                                      |
| instrument_type   | string  | The type of the future instrument. Possible values:                                                                                                                                                                 |
| underlying_symbol | string  | The symbol of the underlying asset.                                                                                                                                                                                 |
| instrument_key    | string  | The unique identifier used across Upstox APIs for instrument identification. For the regex pattern applicable to this field, see the [Field Pattern Appendix](/developer/api-documentation/appendix/field-pattern). |
| lot_size          | number  | The size of one lot of the future.                                                                                                                                                                                  |
| freeze_quantity   | number  | The maximum quantity that can be frozen.                                                                                                                                                                            |
| exchange_token    | string  | The exchange-specific token for the future.                                                                                                                                                                         |
| minimum_lot       | number  | The minimum lot size for the future.                                                                                                                                                                                |
| underlying_key    | string  | The for the underlying asset.                                                                                                                                                                                       |
| tick_size         | number  | The minimum price movement of the future.                                                                                                                                                                           |
| underlying_type   | string  | The type of the underlying asset. Possible values: , , , ,                                                                                                                                                          |
| trading_symbol    | string  | The symbol used for trading the future. Format:                                                                                                                                                                     |

Note

- When you're searching for instrument keys within an instrument JSON file, you can employ the and parameters to refine and narrow down the list of instrument keys. For instance, if you're looking for the instrument key for Reliance Call Option, specify the as and the as , excluding other segments and instrument types from your search criteria. If you want to search for Put Option then set as .

### Field Description

| Field Name        | Type    | Description                                                                                                                                                                                                         |
| ----------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| weekly            | boolean | Indicates if the option is weekly.                                                                                                                                                                                  |
| segment           | string  | The market segment of the option. Possible values: , , , , , , , ,                                                                                                                                                  |
| name              | string  | The name of the option.                                                                                                                                                                                             |
| exchange          | string  | Exchange to which the instrument is associated. Possible values: , ,                                                                                                                                                |
| expiry            | date    | The expiry date of the option.                                                                                                                                                                                      |
| instrument_type   | string  | The type of the option instrument. Possible values: ,                                                                                                                                                               |
| underlying_symbol | string  | The symbol of the underlying asset.                                                                                                                                                                                 |
| instrument_key    | string  | The unique identifier used across Upstox APIs for instrument identification. For the regex pattern applicable to this field, see the [Field Pattern Appendix](/developer/api-documentation/appendix/field-pattern). |
| strike_price      | number  | The strike price for the option.                                                                                                                                                                                    |
| lot_size          | number  | The size of one lot of the option.                                                                                                                                                                                  |
| freeze_quantity   | number  | The maximum quantity that can be frozen.                                                                                                                                                                            |
| exchange_token    | string  | The exchange-specific token for the option.                                                                                                                                                                         |
| minimum_lot       | number  | The minimum lot size for the option.                                                                                                                                                                                |
| underlying_key    | string  | The for the underlying asset.                                                                                                                                                                                       |
| tick_size         | number  | The minimum price movement of the option.                                                                                                                                                                           |
| underlying_type   | string  | The type of the underlying asset. Possible values: , , , ,                                                                                                                                                          |
| trading_symbol    | string  | The symbol used for trading the option. Format:                                                                                                                                                                     |

Note

- When you're searching for instrument keys within an instrument JSON file, you can employ the and parameters to refine and narrow down the list of instrument keys. For instance, if you're looking for the instrument key for NSE Index, specify the as and the as , excluding other segments and instrument types from your search criteria.

### Field Description​

| Field Name | Type   | Description                                    |
| ---------- | ------ | ---------------------------------------------- |
| segment    | string | Segment to which the instrument is associated. |

Possible values: , , , , , , , ,  
name| string| The name of the index.  
exchange| string| Exchange to which the instrument is associated.  
Possible values: , ,  
instrument_type| string| The type of the option instrument.  
Possible values:  
instrument_key| string| The unique identifier used across Upstox APIs for instrument identification. For the regex pattern applicable to this field, see the [Field Pattern Appendix](/developer/api-documentation/appendix/field-pattern).  
exchange_token| number| The numerical identifier issued by the exchange representing the instrument.  
trading_symbol| string| Trading symbol for the index.

Note

- The files undergo daily refresh at around 6 AM, and they are only refreshed as needed during the day, which is a seldom occurrence.
- The BOD instrument for the next trading day will not include delisted stocks or expired contracts.

[PreviousSelf Generated](/developer/api-documentation/self-generated-sdk)[NextLogin](/developer/api-documentation/login)

- CSV Files
  - Sample CSV Record
  - Field Description
- JSON files
  - Sample JSON Object
  - Field Description

---

## [Login | Upstox Developer API](https://upstox.com/developer/api-documentation/login)

- [](/developer/api-documentation/)
- [Developer API](/developer/api-documentation/open-api)
- Login

# Login

## [description AuthorizeLogin flow for the API users.](/developer/api-documentation/authorize)## [description Get TokenGet access token for the API user after login.](/developer/api-documentation/get-token)## [description LogoutLogout flow for the API users.](/developer/api-documentation/logout)

NOTE

You also have the option to select [TOTP (Time-based One-Time Password)](https://en.wikipedia.org/wiki/Time-based_one-time_password) as a more secure method for 2FA, compared to the usual SMS OTP, for a safer login. Learn more about activating TOTP on your Upstox account [here](https://help.upstox.com/support/solutions/articles/260346-what-is-totp-and-how-to-enable-totp-for-my-account-from-upstox-web-platform-).

[PreviousInstruments](/developer/api-documentation/instruments)[NextAuthorize](/developer/api-documentation/authorize)

---

## [User | Upstox Developer API](https://upstox.com/developer/api-documentation/user)

- [](/developer/api-documentation/)
- [Developer API](/developer/api-documentation/open-api)
- User

# User

## [description Get ProfileGet user profile related information.](/developer/api-documentation/get-profile)## [description Get Fund And MarginGet user fund related information in equity and commodity market.](/developer/api-documentation/get-user-fund-margin)

[PreviousLogout](/developer/api-documentation/logout)[NextGet Profile](/developer/api-documentation/get-profile)

---

## [Charges | Upstox Developer API](https://upstox.com/developer/api-documentation/charges)

- [](/developer/api-documentation/)
- [Developer API](/developer/api-documentation/open-api)
- Charges

# Charges

## [description Brokerage DetailsCalculate brokerage charges for an order.](/developer/api-documentation/get-brokerage)

[PreviousGet Fund And Margin](/developer/api-documentation/get-user-fund-margin)[NextBrokerage Details](/developer/api-documentation/get-brokerage)

---

## [Orders | Upstox Developer API](https://upstox.com/developer/api-documentation/orders)

- [](/developer/api-documentation/)
- [Developer API](/developer/api-documentation/open-api)
- Orders

# Orders

NOTE

- If you represent a business aiming to incorporate order flow management (including placing, canceling, and modifying orders), please visit the [Uplink Business](/developer/api-documentation/uplink-business/introduction). The direct HTTP order placement API integration is intended for individual API users.

Important

- In adherence to CDSL regulations, customers without a DDPI/POA are obligated to use a combination of the CDSL TPIN and OTP to provide the necessary authorization for the deduction of securities from their demat account when engaging in delivery sale transactions.

## [description Place OrderPlace an order with all possible combinations.](/developer/api-documentation/place-order)## [description Modify OrderModify pending or open orders.](/developer/api-documentation/modify-order)## [description Cancel OrderCancel pending or open orders.](/developer/api-documentation/cancel-order)## [description Get Order DetailsGet the latest status and details for an order.](/developer/api-documentation/get-order-details)## [description Get Order HistoryGet order history for an order.](/developer/api-documentation/get-order-history)## [description Get Order BookGet the list of all orders placed during the day.](/developer/api-documentation/get-order-book)## [description Get TradesGet the list of all trades for the day.](/developer/api-documentation/get-trade-history)## [description Get Order TradesGet the list of trades executed for an order.](/developer/api-documentation/get-trades-by-order)## [description Get Trade HistoryGet the list of historical trades](/developer/api-documentation/get-historical-trades)

[PreviousBrokerage Details](/developer/api-documentation/get-brokerage)[NextPlace Order](/developer/api-documentation/place-order)

---

## [Portfolio | Upstox Developer API](https://upstox.com/developer/api-documentation/portfolio)

- [](/developer/api-documentation/)
- [Developer API](/developer/api-documentation/open-api)
- Portfolio

# Portfolio

## [description Get PositionsGet current positions of the user.](/developer/api-documentation/get-positions)## [description Convert PositionsConvert the margin product of an open position.](/developer/api-documentation/convert-positions)## [description Get HoldingsGet long term holdings of the user.](/developer/api-documentation/get-holdings)

[PreviousGet Trade History](/developer/api-documentation/get-historical-trades)[NextGet Positions](/developer/api-documentation/get-positions)

---

## [Trade Profit And Loss | Upstox Developer API](https://upstox.com/developer/api-documentation/trade-profit-and-loss)

- [](/developer/api-documentation/)
- [Developer API](/developer/api-documentation/open-api)
- Trade Profit And Loss

# Trade Profit And Loss

## [description Get Report Meta DataGet report meta data.](/developer/api-documentation/get-report-meta-data)## [description Get Profit Loss ReportGet profit and loss report.](/developer/api-documentation/get-profit-and-loss-report)## [description Get Trades ChargesGet trade charges.](/developer/api-documentation/get-trade-charges)

[PreviousGet Holdings](/developer/api-documentation/get-holdings)[NextGet Report Meta Data](/developer/api-documentation/get-report-meta-data)

---

## [Historical Data | Upstox Developer API](https://upstox.com/developer/api-documentation/historical-data)

- [](/developer/api-documentation/)
- [Developer API](/developer/api-documentation/open-api)
- Historical Data

# Historical Data

## [description Historical Candle DataGet historical OHLC values for the given instrument.](/developer/api-documentation/get-historical-candle-data)## [description Intraday Candle DataGet present trading day OHLC values for the given instrument.](/developer/api-documentation/get-intra-day-candle-data)

[PreviousGet Trades Charges](/developer/api-documentation/get-trade-charges)[NextHistorical Candle Data](/developer/api-documentation/get-historical-candle-data)

---

## [Market Quote | Upstox Developer API](https://upstox.com/developer/api-documentation/market-quote)

- [](/developer/api-documentation/)
- [Developer API](/developer/api-documentation/open-api)
- Market Quote

# Market Quote

## [description Full Market QuotesGet full market quotes for one or more instruments.](/developer/api-documentation/get-full-market-quote)## [description OHLC QuotesGet OHLC quotes for one or more instruments.](/developer/api-documentation/get-market-quote-ohlc)## [description LTP QuotesGet the LTP quotes for one or more instruments.](/developer/api-documentation/ltp)

[PreviousIntraday Candle Data](/developer/api-documentation/get-intra-day-candle-data)[NextFull Market Quotes](/developer/api-documentation/get-full-market-quote)

---

## [Market Information | Upstox Developer API](https://upstox.com/developer/api-documentation/market-information)

- [](/developer/api-documentation/)
- [Developer API](/developer/api-documentation/open-api)
- Market Information

# Market Information

## [description Market HolidaysGet holiday list for the current year](/developer/api-documentation/get-market-holidays)## [description Market TimingsGet market timing list for particular date](/developer/api-documentation/get-market-timings)## [description Exchange StatusGet market status for particular exchange.](/developer/api-documentation/get-market-status)

[PreviousLTP Quotes](/developer/api-documentation/ltp)[NextMarket Holidays](/developer/api-documentation/get-market-holidays)

---

## [Option Chain | Upstox Developer API](https://upstox.com/developer/api-documentation/option-chain)

- [](/developer/api-documentation/)
- [Developer API](/developer/api-documentation/open-api)
- Option Chain

# Option Chain

## [description Option ContractsGet option contracts](/developer/api-documentation/get-option-contracts)## [description Put/Call Option chainGet Put/Call option chain](/developer/api-documentation/get-pc-option-chain)

[PreviousExchange Status](/developer/api-documentation/get-market-status)[NextOption Contracts](/developer/api-documentation/get-option-contracts)

---

## [Websocket | Upstox Developer API](https://upstox.com/developer/api-documentation/websocket)

- [](/developer/api-documentation/)
- [Developer API](/developer/api-documentation/open-api)
- Websocket

# Websocket

## [description Portfolio Stream FeedGet live order updates.](/developer/api-documentation/get-portfolio-stream-feed)## [description Get Portfolio Stream Feed Authorized UrlGet live order updates socket endpoint Url.](/developer/api-documentation/get-portfolio-stream-feed-authorize)## [description Market Data FeedGet live market data.](/developer/api-documentation/get-market-data-feed)## [description Get Market Data Feed Authorized UrlGet live market socket endpoint Url.](/developer/api-documentation/get-market-data-feed-authorize)

[PreviousPut/Call Option chain](/developer/api-documentation/get-pc-option-chain)[NextPortfolio Stream Feed](/developer/api-documentation/get-portfolio-stream-feed)

---

## [Websocket Implementation | Upstox Developer API](https://upstox.com/developer/api-documentation/websocket-implementation)

- [](/developer/api-documentation/)
- [Developer API](/developer/api-documentation/open-api)
- Websocket implementation

# Websocket Implementation

The websocket streaming provides an efficient way to receive market and order related communication over a long standing connection.

Websockets offer several technical advantages over standard API calls:

- Efficiency: Instead of repeatedly polling for data, websockets allow data to be pushed to the client as it becomes available.
- Real-time: Websockets provide real-time communication which is crucial for trading applications where every second counts.
- Reduced overhead: With websockets, the overhead of establishing a connection is reduced as one connection can be kept open for longer durations.

Websockets should be preferred when:

- Real-time updates are required.
- The frequency of data updates is high, making regular API polling inefficient.
- Reducing network overhead is a priority.

We provide two types of streaming options:

- Market related changes for the subscribed entities
- Order related updates

## [description Sample ImplementationSample implementation available in Python, PHP, Node Js and Java.](/developer/api-documentation/sample-implementation)

[PreviousGet Market Data Feed Authorized Url](/developer/api-documentation/get-market-data-feed-authorize)[NextSample Implementation](/developer/api-documentation/sample-implementation)

---

## [Webhook | Upstox Developer API](https://upstox.com/developer/api-documentation/webhook)

- [](/developer/api-documentation/)
- [Developer API](/developer/api-documentation/open-api)
- Webhook

On this page

# Webhook

During the app registration process, users have the option to specify an open POST API as their webhook URL. If they choose to provide such a URL, all order updates will be promptly transmitted to this address. This endpoint is not required to have any authentication mechanisms in place, and it should respond with either a basic string or a JSON object. The payload sent by Upstox API to the webhook URL will be identical to the [Order Stream Updates](/developer/api-documentation/get-portfolio-stream-feed#message-structure) that are typically transmitted via WebSocket.

## Response structure:​

Notice of Deprecation

The lowercase field () is deprecated and will be removed in future versions. Use the snake_case versions for consistency.

NOTE

- While creating app provide a webhook URL which is in your control rather than a public endpoint.

[PreviousSample Implementation](/developer/api-documentation/sample-implementation)[NextAppendix](/developer/api-documentation/appendix)

- Response structure:

---

## [Appendix | Upstox Developer API](https://upstox.com/developer/api-documentation/appendix)

- [](/developer/api-documentation/)
- [Developer API](/developer/api-documentation/open-api)
- Appendix

# Appendix

## [description Postman CollectionGet started with Postman collection.](/developer/api-documentation/appendix/postman-collection)## [description Equity Security TypeList of all the possible security type for an equity instrument.](/developer/api-documentation/appendix/equity-security-type)## [description ExchangeList of all supported exchanges.](/developer/api-documentation/appendix/exchange)## [description Market StatusList of all the possible market status.](/developer/api-documentation/appendix/market-status)## [description Order StatusList of all the possible order status.](/developer/api-documentation/appendix/order-status)## [description Field PatternList of fields inputs patterns required in API.](/developer/api-documentation/appendix/field-pattern)## [description ChangelogChangelog](/developer/api-documentation/appendix/change-log)## [link TOTP Login](https://help.upstox.com/support/solutions/articles/260346-what-is-totp-and-how-to-enable-totp-for-my-account-from-upstox-web-platform-)## [link Developer Community](https://community.upstox.com/c/developer-api/15)[PreviousWebhook](/developer/api-documentation/webhook)[NextPostman Collection](/developer/api-documentation/appendix/postman-collection)

---

## [Uplink Business | Upstox Developer API](https://upstox.com/developer/api-documentation/uplink-business/introduction#docusaurus_skipToContent_fallback)

- [](/developer/api-documentation/)
- UpLink Business

# Uplink Business

UpLink Business is the middleware that helps all multi-clients to place orders through Upstox’s platform complying with the latest SEBI norms.

New to UpLink Business?

- To use UpLink Business, you would need a multi-client API which is created on-demand for our business partners.
- To request for a multi-client API, you can either [fill the form](https://upstox.com/uplink/business-trading-api/) on UpLink Business webpage or create a thread on [Upstox Community](https://community.upstox.com/).

## [description Place OrderPlace an order with all possible combinations.](/developer/api-documentation/uplink-business/docs/place-order)## [description Modify OrderModify pending or open orders.](/developer/api-documentation/uplink-business/docs/modify-order)## [description Cancel OrderCancel pending or open orders.](/developer/api-documentation/uplink-business/docs/cancel-order)## [description CDSL AuthCDSL authorization steps for delivery sale transactions.](/developer/api-documentation/uplink-business/docs/cdsl-auth)

NOTE

- When dealing with a multi-client application, the process of placing, canceling, or modifying orders necessitates the use of the Uplink Business approach. This method involves utilizing an HTML form containing order details, which is then submitted to the Uplink UI. The subsequent order processing tasks are efficiently managed by the Uplink UI.
- It's important to note that employing the order API for order placement is not permissible with a multi-client app. Attempting to do so will trigger an error message stating, ""Access to this API has been restricted for your account. Please use 'Uplink Business' to place/modify/cancel the order."

[NextPlace Order](/developer/api-documentation/uplink-business/docs/place-order)

---

## [Place Order | Upstox Developer API](https://upstox.com/developer/api-documentation/uplink-business/docs/place-order)

- [](/developer/api-documentation/)
- [UpLink Business](/developer/api-documentation/uplink-business/introduction)
- Place Order

On this page

# Place Order

## Client application​

![Client application place order](data:image/webp;base64,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)

Considering a client application like the one provided above, the client has to provide the access token and order details to UpLink business. The client receives the access token while authenticating the user through Upstox Developer API login.

### Sample orders​

### Sample request​

NOTE

- The Upstox developer API access token represents the token acquired through the [Get Token API](/developer/api-documentation/get-token) after logging in.
- When using the Uplink Business, please refrain from including the prefix before the Upstox developer API access token.
- In adherence to CDSL regulations, customers without a DDPI/POA are obligated to use a combination of the CDSL TPIN and OTP to provide the necessary authorization for the deduction of securities from their demat account when engaging in delivery sale transactions.

### Order parameters mapping​

| Key                | Required | Description                                                                                                                                                   |
| ------------------ | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| is_amo             | required | Signifies if the order is an After Market Order (boolean).                                                                                                    |
| instrument_token   | required | Key of the instrument. For the regex pattern applicable to this field, see the [Field Pattern Appendix](/developer/api-documentation/appendix/field-pattern). |
| validity           | required | It can be one of the following - DAY(default), IOC.                                                                                                           |
| transaction_type   | required | BUY or SELL.                                                                                                                                                  |
| order_type         | required | Order type (MARKET, LIMIT, SL, SL-M).                                                                                                                         |
| quantity           | required | Quantity with which the order is to be placed.                                                                                                                |
| product            | required | Signifies if the order was either Intraday, Delivery, CO or OCO.                                                                                              |
| price              | optional | Price at which the order will be placed for LIMIT orders.                                                                                                     |
| trigger_price      | optional | For SL, SL-M etc.                                                                                                                                             |
| disclosed_quantity | optional | The quantity that should be disclosed in the market depth.                                                                                                    |
| tag                | optional | Tag to uniquely identify an order.                                                                                                                            |

UpLink business takes the required access token, list of orders and redirect url as query parameters.

## UpLink business application​

UpLink business reads the provided query parameters and renders the data for user confirmation to place the order.

![UpLink business application place order](/developer/api-documentation/assets/images/place-order-8b9cdd3be505df0cc9438cbc064f328d.webp)

Before placing the order, the user is still allowed to edit the order.

When the user clicks on “Edit Order“ button, it takes them to edit page. Here the user is allowed to delete individual orders.

![UpLink business application edit order](data:image/webp;base64,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)

When the user clicks or taps on the bin icon against each order, it asks for confirmation.

![UpLink business application delete order](/developer/api-documentation/assets/images/delete-order-f9330c890b9995cacf5e15c16fad1447.webp)

When the user confirms to delete by tapping or clicking on 'Delete', a success toast message is shown.

![UpLink business application delete order success](data:image/webp;base64,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)

Then, the user is taken back to review order screen.

![UpLink business application review order](/developer/api-documentation/assets/images/review-order-8b9cdd3be505df0cc9438cbc064f328d.webp)

When the user taps or clicks on 'Show charges', they can view all brokerage and transaction charges involved in placing the orders.

![UpLink business application order charges](/developer/api-documentation/assets/images/charges-2d05800eaad3109e4ff263bfe1fa5ddd.webp)

When the user taps or clicks on 'Place order', they can place the order with Upstox. Once placed, they will be provided with the status of each order.

![UpLink business application order charges](/developer/api-documentation/assets/images/order-status-8ac3c24a9adbf7030825e810075dc245.webp)

If the user deletes all orders or has no orders to review, an exit screen is shown.

![UpLink business application order charges](data:image/webp;base64,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zZwlFFixYsWLFixYsWwyKcOHDhw4cOHDhw9GnDhw4cOHDhw4cOHDi0F69evXr169evXsA7qFChQoUKFChQoUKFChQoUKFChQoUKFChRRJ4sWLFixYsWLFi375qcOHDhw4cOHDhw4cOHDhw4cOHDhw4cOHbShfv379+/fv37+CvxOCxYsWLFixYsWLFixYsWLFixYsWLFixY5nzU4cOHDhw4cOHFoL169evXr169evXr169evXr169evXr169e3KAoUKFChQoUKFCiiTxYsWLFixYsWLFixYsWLFixYsWLFixYsWPss6dOnTp06dOnTqj7+/fv379+/fv379+/fv379+/fv379+/fv6nbO6cFixYsWLFixuoUFIVWDsMhkMhkMhkMhkMhkMluwkQUH3/OO4YSINxz4VhpsE3LbtycYJtFixYsWLFixYscz9GS8WOpeBJ9/sJZeLHUvAk++wzJiayQ70H7xiRAcogW7pkFgIdZADnr169evXr169gIbNNmzZs2bNmzZs2bNbPoAP+W7s4u1Kdzq3d8uudQ1M0KcTVLAFh7hbqgScIA540kyQR+tBu7/gFNznDpRPq0DwDM5NMxLzpUImnhi+CjtEUMx4NlCWnTp06dOnTp06fEd5aLFixYsWLFixYsWLRZcJqX8xfv379+38EUwholp06dOnTp06dOntniYGD1Pnsm3cTigSCvR95tJheKDIan+/4DjrilWf4t/fk/PYPvFgojTamqfHGTsRLjMWLFixYsWLFikIKO4LHkefxJZ3DPbjVzAyax9rt14HGxFt8gN59+zx4+EKv037/CFX6b9/f84hOnTp06dOnTp06dPeMvRyORyORyORyORyORyORyORyORyORyORyORyORyOQxmpw4cOG6AAA/q7a6xcVN19WAAAbYsuVsth+pMkTZKefOrh7uHj4rdigA3VdYtOALz5Qn72Ip9+jeFSi8IlqSABWNA4ONajNvs2xxidWtHf/UvuovSxKrUT5RfH24eP4g+Fqs1NQ5iEdP2lUrn7wQrT16IzE4FIDskiL4/k1frVCbOul59pqA9imxss+wt+WTKvtb0dKLZhG6YZjV0KvTMYqNhU1Gx6dE/nZn9cHxlKav63AF0qU1O3Kt9Mz/jMX7xBne3Q3KZHpk5lh33YU+okzRC97iPlJjCFhmaxLgZY8TFeq8fO84CfB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)

After placing the order, if the user clicks or taps on 'Exit' or 'Done', they will be redirected to the client provided redirect URL.

[PreviousUplink Business](/developer/api-documentation/uplink-business/introduction)[NextModify Order](/developer/api-documentation/uplink-business/docs/modify-order)

- Client application
  - Sample orders
  - Sample request
  - Order parameters mapping
- UpLink business application

---

## [Modify Order | Upstox Developer API](https://upstox.com/developer/api-documentation/uplink-business/docs/modify-order)

- [](/developer/api-documentation/)
- [UpLink Business](/developer/api-documentation/uplink-business/introduction)
- Modify Order

On this page

# Modify Order

## Sample request​

NOTE

- Unlike place order, modification of only one order is allowed per transaction.
- Order details are retrieved using the provided in the request and made available in the Uplink UI for user to proceed with the modification.

[PreviousPlace Order](/developer/api-documentation/uplink-business/docs/place-order)[NextCancel Order](/developer/api-documentation/uplink-business/docs/cancel-order)

- Sample request

---

## [Cancel Order | Upstox Developer API](https://upstox.com/developer/api-documentation/uplink-business/docs/cancel-order)

- [](/developer/api-documentation/)
- [UpLink Business](/developer/api-documentation/uplink-business/introduction)
- Cancel Order

On this page

# Cancel Order

## Client application​

![Client application cancel order](/developer/api-documentation/assets/images/client-cancel-order-18e79bbc1807b9b8644fefd593df73e8.webp)

The client has to provide the access token and order ID to UpLink Business.

### Sample request​

## UpLink business application​

![UpLink business application cancel order](/developer/api-documentation/assets/images/cancel-order-008a03a7103409272be7eeb2e5f98105.webp)

Once the request is sent to UpLink business, it validates the status of the order. If the order can be cancelled, the user is provided with above pop-up message. After confirming by tapping or clicking on 'Yes, cancel', the order gets cancelled.

![UpLink business application cancel order success](data:image/webp;base64,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)

If the user clicks or taps on 'Done', they will be redirected to the the client application using the redirect_url provided in the request.

NOTE

Unlike place order, cancellation of only one order is allowed per transaction.

[PreviousModify Order](/developer/api-documentation/uplink-business/docs/modify-order)[NextCDSL Auth](/developer/api-documentation/uplink-business/docs/cdsl-auth)

- Client application
  - Sample request
- UpLink business application

---

## [CDSL Auth | Upstox Developer API](https://upstox.com/developer/api-documentation/uplink-business/docs/cdsl-auth)

- [](/developer/api-documentation/)
- [UpLink Business](/developer/api-documentation/uplink-business/introduction)
- CDSL Auth

# CDSL Auth

CDSL authorisation workflow starts from review screen. This entire process is handled within UpLink business application. There is no integration needed from client.

From client application, the user is taken to “Review orders” screen. After all editing is done, once the client clicks on “Place order”, UpLink business asks the user to authorise to check the status of CDSL permissions.

![UpLink business cdsl authentication](/developer/api-documentation/assets/images/cdsl-auth-eb1151f2897092436556c064211bd5c4.webp)

When the user clicks on “Authorise & place order“ the user is taken to an info screen which gives information on how to generate PIN required for authorisation.

![UpLink business cdsl authorisation information](/developer/api-documentation/assets/images/cdsl-page-12d46c588e3cf7c90f36812f919e0c81.webp)

One the user completes the registration and generates a pin, the user has to click on “Continue to CDSL“. Now the user will be taken “TPIN“ verification page.

![CDSL TPIN](data:image/webp;base64,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)

Important

- In adherence to CDSL regulations, customers without a DDPI/POA are obligated to use a combination of the CDSL TPIN and OTP to provide the necessary authorization for the deduction of securities from their demat account when engaging in delivery sale transactions.

The user has to enter the TPIN and click “verify“ to authorise the order transaction. Once the status is verified, the user will be taken back to “review orders” screen.

![UpLink business application review order cdsl success](/developer/api-documentation/assets/images/cdsl-success-55d86b0e941b957b1a7169f4d573185a.webp)

An authorisation success message toast is shown and the user can place a sell order now.

[PreviousCancel Order](/developer/api-documentation/uplink-business/docs/cancel-order)

---

## [Example Code | Upstox Developer API](https://upstox.com/developer/api-documentation/example-code/introduction#docusaurus_skipToContent_fallback)

- [](/developer/api-documentation/)
- Example Code

# Example Code

## [folder Login2 items](/developer/api-documentation/example-code/login/get-token)## [folder User2 items](/developer/api-documentation/example-code/user/get-profile)## [folder Charges1 items](/developer/api-documentation/example-code/charges/brokerage-details)## [folder Order9 items](/developer/api-documentation/example-code/orders/place-order)## [folder Portfolio3 items](/developer/api-documentation/example-code/portfolio/convert-positions)## [folder Trade Profit and Loss3 items](/developer/api-documentation/example-code/trade-profit-and-loss/get-report-meta-data)## [folder Historical Data2 items](/developer/api-documentation/example-code/historical-data/historical-candle-data)## [folder Market Quote3 items](/developer/api-documentation/example-code/market-quote/full-market-quotes)## [folder Market Information3 items](/developer/api-documentation/example-code/market-information/market-holidays)## [folder Option Chain2 items](/developer/api-documentation/example-code/option-chain/option-contracts)

[NextGet Token](/developer/api-documentation/example-code/login/get-token)

---

## [Get Token | Upstox Developer API](https://upstox.com/developer/api-documentation/example-code/login/get-token)

- [](/developer/api-documentation/)
- [Example Code](/developer/api-documentation/example-code/introduction)
- Login
- Get Token

On this page

# Get Token

## Get access token using auth code​

- Curl
- Python
- Node.js
- Java
- PHP
- Python SDK
- Node.js SDK
- Java SDK

  **Node.js Code:**

  **Node.js Code:**

  const axios = require('axios');

  const url = 'https://api.upstox.com/v2/login/authorization/token';  
  const headers = {  
   'accept': 'application/json',  
   'Content-Type': 'application/x-www-form-urlencoded',  
  };

  const data = {  
   'code': '{your_code}',  
   'client_id': '{your_client_id}',  
   'client_secret': '{your_client_secret}',  
   'redirect_uri': '{your_redirect_url}',  
   'grant_type': 'authorization_code',  
  };

  axios.post(url, new URLSearchParams(data), { headers })  
   .then(response => {  
   console.log(response.status);  
   console.log(response.data);  
   })  
   .catch(error => {  
   console.error(error.response.status);  
   console.error(error.response.data);  
   });

  **Node.js Code:**

  **Node.js Code:**

  let UpstoxClient = require('upstox-js-sdk');

  let apiInstance = new UpstoxClient.LoginApi();  
  let apiVersion = "2.0";  
  let opts = {  
   'code': "{your_auth_code}",  
   'clientId': "{your_client_secret}",  
   'clientSecret': "{your_client_secret}",  
   'redirectUri': "{your_redirect_url}",  
   'grantType': "authorization_code"  
  };  
  apiInstance.token(apiVersion, opts, (error, data, response) => {  
   if (error) {  
   console.error(error);  
   } else {  
   console.log('API called successfully. Returned data: ' + JSON.stringify(data));  
   }  
  });

[PreviousExample Code](/developer/api-documentation/example-code/introduction)[NextLogout](/developer/api-documentation/example-code/login/logout)

- Get access token using auth code

---

## [Get Profile | Upstox Developer API](https://upstox.com/developer/api-documentation/example-code/user/get-profile)

- [](/developer/api-documentation/)
- [Example Code](/developer/api-documentation/example-code/introduction)
- User
- Get Profile

On this page

# Get Profile

## Get user profile information using access token​

- Curl
- Python
- Node.js
- Java
- PHP
- Python SDK
- Node.js SDK
- Java SDK

  **Node.js Code:**

  **Node.js Code:**

  const axios = require('axios');

  const url = 'https://api.upstox.com/v2/user/profile';  
  const headers = {  
   'Accept': 'application/json',  
   'Authorization': 'Bearer {your_access_token}'  
  };

  axios.get(url, { headers })  
   .then(response => {  
   console.log(response.status);  
   console.log(response.data);  
   })  
   .catch(error => {  
   console.error(error);  
   });

  **Node.js Code:**

  **Node.js Code:**

  let UpstoxClient = require('upstox-js-sdk');  
  let defaultClient = UpstoxClient.ApiClient.instance;  
  var OAUTH2 = defaultClient.authentications['OAUTH2'];  
  OAUTH2.accessToken = "{your_access_token}";  
  let apiInstance = new UpstoxClient.UserApi();  
  let apiVersion = "2.0"; // String | API Version Header  
  apiInstance.getProfile(apiVersion, (error, data, response) => {  
   if (error) {  
   console.error(error);  
   } else {  
   console.log('API called successfully. Returned data: ' + JSON.stringify(data));  
   }  
  });

[PreviousLogout](/developer/api-documentation/example-code/login/logout)[NextGet Fund and Margin](/developer/api-documentation/example-code/user/get-fund-and-margin)

- Get user profile information using access token

---

## [Brokerage Details | Upstox Developer API](https://upstox.com/developer/api-documentation/example-code/charges/brokerage-details)

- [](/developer/api-documentation/)
- [Example Code](/developer/api-documentation/example-code/introduction)
- Charges
- Brokerage Details

On this page

# Brokerage Details

## Get brokerage details for equity delivery orders​

- Curl
- Python
- Node.js
- Java
- PHP
- Python SDK
- Node.js SDK
- Java SDK

  **Node.js Code:**

  **Node.js Code:**

  const axios = require('axios');

  const url = 'https://api.upstox.com/v2/charges/brokerage';  
  const headers = {  
   'Accept': 'application/json',  
   'Authorization': 'Bearer {your_access_token}'  
  };

  const params = {  
   instrument_token: 'NSE_EQ|INE669E01016',  
   quantity: '10',  
   product: 'D',  
   transaction_type: 'BUY',  
   price: '13.7'  
  };

  axios.get(url, { headers, params })  
   .then(response => {  
   console.log(response.data);  
   })  
   .catch(error => {  
   console.error(error.message);  
   });

  **Node.js Code:**

  **Node.js Code:**

  let UpstoxClient = require('upstox-js-sdk');  
  let defaultClient = UpstoxClient.ApiClient.instance;  
  var OAUTH2 = defaultClient.authentications['OAUTH2'];  
  OAUTH2.accessToken = "{your_access_token}";

  let apiInstance = new UpstoxClient.ChargeApi();  
  let instrumentToken = "NSE_EQ|INE669E01016";  
  let quantity = 56;  
  let product = "D";  
  let transactionType = "BUY";  
  let price = 23.4;  
  let apiVersion = "2.0";

  apiInstance.getBrokerage(instrumentToken, quantity, product, transactionType, price, apiVersion, (error, data, response) => {  
   if (error) {  
   console.error(error);  
   } else {  
   console.log('API called successfully. Returned data: ' + JSON.stringify(data));  
   }  
  });

## Get brokerage details for equity intraday orders​

- Curl
- Python
- Node.js
- Java
- PHP
- Python SDK
- Node.js SDK
- Java SDK

  **Node.js Code:**

  **Node.js Code:**

  const axios = require('axios');

  const url = 'https://api.upstox.com/v2/charges/brokerage';  
  const headers = {  
   'Accept': 'application/json',  
   'Authorization': 'Bearer {your_access_token}'  
  };

  const params = {  
   instrument_token: 'NSE_EQ|INE669E01016',  
   quantity: '10',  
   product: 'I',  
   transaction_type: 'BUY',  
   price: '13.7'  
  };

  axios.get(url, { headers, params })  
   .then(response => {  
   console.log(response.data);  
   })  
   .catch(error => {  
   console.error(error.message);  
   });

  **Node.js Code:**

  **Node.js Code:**

  let UpstoxClient = require('upstox-js-sdk');  
  let defaultClient = UpstoxClient.ApiClient.instance;  
  var OAUTH2 = defaultClient.authentications['OAUTH2'];  
  OAUTH2.accessToken = "{your_access_token}";

  let apiInstance = new UpstoxClient.ChargeApi();  
  let instrumentToken = "NSE_EQ|INE669E01016";  
  let quantity = 10;  
  let product = "I";  
  let transactionType = "BUY";  
  let price = 20.4;  
  let apiVersion = "2.0";

  apiInstance.getBrokerage(instrumentToken, quantity, product, transactionType, price, apiVersion, (error, data, response) => {  
   if (error) {  
   console.error(error);  
   } else {  
   console.log('API called successfully. Returned data: ' + JSON.stringify(data));  
   }  
  });

## Get brokerage details for equity futures and options delivery orders​

- Curl
- Python
- Node.js
- Java
- PHP
- Python SDK
- Node.js SDK
- Java SDK

  **Node.js Code:**

  **Node.js Code:**

  const axios = require('axios');

  const url = 'https://api.upstox.com/v2/charges/brokerage';  
  const headers = {  
   'Accept': 'application/json',  
   'Authorization': 'Bearer {your_access_token}'  
  };

  const params = {  
   'instrument_token': 'NSE_FO|35271',  
   'quantity': '10',  
   'product': 'D',  
   'transaction_type': 'BUY',  
   'price': '1400'  
  };

  axios.get(url, { headers, params })  
   .then(response => {  
   console.log(response.status);  
   console.log(response.data);  
   })  
   .catch(error => {  
   console.error(error.response.status);  
   console.error(error.response.data);  
   });

  **Node.js Code:**

  **Node.js Code:**

  let UpstoxClient = require('upstox-js-sdk');  
  let defaultClient = UpstoxClient.ApiClient.instance;  
  var OAUTH2 = defaultClient.authentications['OAUTH2'];  
  OAUTH2.accessToken = "{your_access_token}";

  let apiInstance = new UpstoxClient.ChargeApi();  
  let instrumentToken = "NSE_FO|35271";  
  let quantity = 10;  
  let product = "D";  
  let transactionType = "BUY";  
  let price = 2000.4;  
  let apiVersion = "2.0";

  apiInstance.getBrokerage(instrumentToken, quantity, product, transactionType, price, apiVersion, (error, data, response) => {  
   if (error) {  
   console.error(error);  
   } else {  
   console.log('API called successfully. Returned data: ' + JSON.stringify(data));  
   }  
  });

## Get brokerage details for equity futures and options intraday orders​

- Curl
- Python
- Node.js
- Java
- PHP
- Python SDK
- Node.js SDK
- Java SDK

  **Node.js Code:**

  **Node.js Code:**

  const axios = require('axios');

  const url = 'https://api.upstox.com/v2/charges/brokerage';  
  const headers = {  
   'Accept': 'application/json',  
   'Authorization': 'Bearer {your_access_token}'  
  };

  const params = {  
   'instrument_token': 'NSE_FO|35271',  
   'quantity': '10',  
   'product': 'I',  
   'transaction_type': 'BUY',  
   'price': '1400'  
  };

  axios.get(url, { headers, params })  
   .then(response => {  
   console.log(response.status);  
   console.log(response.data);  
   })  
   .catch(error => {  
   console.error(error.response.status);  
   console.error(error.response.data);  
   });

  **Node.js Code:**

  **Node.js Code:**

  let UpstoxClient = require('upstox-js-sdk');  
  let defaultClient = UpstoxClient.ApiClient.instance;  
  var OAUTH2 = defaultClient.authentications['OAUTH2'];  
  OAUTH2.accessToken = "{your_access_token}";

  let apiInstance = new UpstoxClient.ChargeApi();  
  let instrumentToken = "NSE_FO|35271";  
  let quantity = 10;  
  let product = "I";  
  let transactionType = "BUY";  
  let price = 2000.4;  
  let apiVersion = "2.0";

  apiInstance.getBrokerage(instrumentToken, quantity, product, transactionType, price, apiVersion, (error, data, response) => {  
   if (error) {  
   console.error(error);  
   } else {  
   console.log('API called successfully. Returned data: ' + JSON.stringify(data));  
   }  
  });

[PreviousGet Fund and Margin](/developer/api-documentation/example-code/user/get-fund-and-margin)[NextPlace Order](/developer/api-documentation/example-code/orders/place-order)

- Get brokerage details for equity delivery orders
- Get brokerage details for equity intraday orders
- Get brokerage details for equity futures and options delivery orders
- Get brokerage details for equity futures and options intraday orders

---

## [Place Order | Upstox Developer API](https://upstox.com/developer/api-documentation/example-code/orders/place-order)

- [](/developer/api-documentation/)
- [Example Code](/developer/api-documentation/example-code/introduction)
- Order
- Place Order

On this page

# Place Order

## Place a delivery market order​

- Curl
- Python
- Node.js
- Java
- PHP
- Python SDK
- Node.js SDK
- Java SDK

  **Node.js Code:**

  **Node.js Code:**

  const axios = require('axios');

  const url = 'https://api.upstox.com/v2/order/place';  
  const headers = {  
   'Content-Type': 'application/json',  
   'Accept': 'application/json',  
   'Authorization': 'Bearer {your_access_token}',  
  };

  const data = {  
   quantity: 1,  
   product: 'D',  
   validity: 'DAY',  
   price: 0,  
   tag: 'string',  
   instrument_token: 'NSE_EQ|INE669E01016',  
   order_type: 'MARKET',  
   transaction_type: 'BUY',  
   disclosed_quantity: 0,  
   trigger_price: 0,  
   is_amo: false,  
  };

  axios.post(url, data, { headers })  
   .then(response => {  
   console.log('Response:', response.data);  
   })  
   .catch(error => {  
   console.error('Error:', error.message);  
   });

  **Node.js Code:**

  **Node.js Code:**

  let UpstoxClient = require('upstox-js-sdk');  
  let defaultClient = UpstoxClient.ApiClient.instance;  
  var OAUTH2 = defaultClient.authentications['OAUTH2'];  
  OAUTH2.accessToken = "{your_access_token}";

  let apiInstance = new UpstoxClient.OrderApi();  
  let body = new UpstoxClient.PlaceOrderRequest(1, UpstoxClient.PlaceOrderRequest.ProductEnum.D, UpstoxClient.PlaceOrderRequest.ValidityEnum.DAY, 0.0, "NSE_EQ|INE528G01035",UpstoxClient.PlaceOrderRequest.OrderTypeEnum.MARKET,UpstoxClient.PlaceOrderRequest.TransactionTypeEnum.BUY, 0, 0.0, false);  
  let apiVersion = "2.0";

  apiInstance.placeOrder(body, apiVersion, (error, data, response) => {  
   if (error) {  
   console.error(error.response.text);  
   } else {  
   console.log('API called successfully. Returned data: ' + data);  
   }  
  });

## Place a delivery limit order​

- Curl
- Python
- Node.js
- Java
- PHP
- Python SDK
- Node.js SDK
- Java SDK

  **Node.js Code:**

  **Node.js Code:**

  const axios = require('axios');

  const url = 'https://api.upstox.com/v2/order/place';  
  const headers = {  
   'Content-Type': 'application/json',  
   'Accept': 'application/json',  
   'Authorization': 'Bearer {your_access_token}',  
  };

  const data = {  
   quantity: 1,  
   product: 'D',  
   validity: 'DAY',  
   price: 13,  
   tag: 'string',  
   instrument_token: 'NSE_EQ|INE669E01016',  
   order_type: 'LIMIT',  
   transaction_type: 'BUY',  
   disclosed_quantity: 0,  
   trigger_price: 13.2,  
   is_amo: false,  
  };

  axios.post(url, data, { headers })  
   .then(response => {  
   console.log('Response:', response.data);  
   })  
   .catch(error => {  
   console.error('Error:', error.message);  
   });

  **Node.js Code:**

  **Node.js Code:**

  let UpstoxClient = require('upstox-js-sdk');  
  let defaultClient = UpstoxClient.ApiClient.instance;  
  var OAUTH2 = defaultClient.authentications['OAUTH2'];  
  OAUTH2.accessToken = "{your_access_token}";

  let apiInstance = new UpstoxClient.OrderApi();  
  let body = new UpstoxClient.PlaceOrderRequest(1, UpstoxClient.PlaceOrderRequest.ProductEnum.D, UpstoxClient.PlaceOrderRequest.ValidityEnum.DAY, 20.0, "NSE_EQ|INE528G01035",UpstoxClient.PlaceOrderRequest.OrderTypeEnum.LIMIT,UpstoxClient.PlaceOrderRequest.TransactionTypeEnum.BUY, 0, 20.1, false);  
  let apiVersion = "2.0";

  apiInstance.placeOrder(body, apiVersion, (error, data, response) => {  
   if (error) {  
   console.error(error.response.text);  
   } else {  
   console.log('API called successfully. Returned data: ' + data);  
   }  
  });

## Place a delivery stop-loss order​

- Curl
- Python
- Node.js
- Java
- PHP
- Python SDK
- Node.js SDK
- Java SDK

  **Node.js Code:**

  **Node.js Code:**

  const axios = require('axios');

  const url = 'https://api.upstox.com/v2/order/place';  
  const headers = {  
   'Content-Type': 'application/json',  
   'Accept': 'application/json',  
   'Authorization': 'Bearer {your_access_token}',  
  };

  const data = {  
   quantity: 1,  
   product: 'D',  
   validity: 'DAY',  
   price: 14.05,  
   tag: 'string',  
   instrument_token: 'NSE_EQ|INE669E01016',  
   order_type: 'SL',  
   transaction_type: 'BUY',  
   disclosed_quantity: 0,  
   trigger_price: 13,  
   is_amo: false,  
  };

  axios.post(url, data, { headers })  
   .then(response => {  
   console.log('Response:', response.data);  
   })  
   .catch(error => {  
   console.error('Error:', error.message);  
   });

  **Node.js Code:**

  **Node.js Code:**

  let UpstoxClient = require('upstox-js-sdk');  
  let defaultClient = UpstoxClient.ApiClient.instance;  
  var OAUTH2 = defaultClient.authentications['OAUTH2'];  
  OAUTH2.accessToken = "{your_access_token}";

  let apiInstance = new UpstoxClient.OrderApi();  
  let body = new UpstoxClient.PlaceOrderRequest(1, UpstoxClient.PlaceOrderRequest.ProductEnum.D, UpstoxClient.PlaceOrderRequest.ValidityEnum.DAY, 20.0, "NSE_EQ|INE528G01035",UpstoxClient.PlaceOrderRequest.OrderTypeEnum.SL,UpstoxClient.PlaceOrderRequest.TransactionTypeEnum.BUY, 0, 19.5, false);  
  let apiVersion = "2.0";

  apiInstance.placeOrder(body, apiVersion, (error, data, response) => {  
   if (error) {  
   console.error(error.response.text);  
   } else {  
   console.log('API called successfully. Returned data: ' + data);  
   }  
  });

## Place a delivery stop-loss order market​

- Curl
- Python
- Node.js
- Java
- PHP
- Python SDK
- Node.js SDK
- Java SDK

  **Node.js Code:**

  **Node.js Code:**

  const axios = require('axios');

  const url = 'https://api.upstox.com/v2/order/place';  
  const headers = {  
   'Content-Type': 'application/json',  
   'Accept': 'application/json',  
   'Authorization': 'Bearer {your_access_token}',  
  };

  const data = {  
   quantity: 1,  
   product: 'D',  
   validity: 'DAY',  
   price: 0.0,  
   tag: 'string',  
   instrument_token: 'NSE_EQ|INE669E01016',  
   order_type: 'SL-M',  
   transaction_type: 'BUY',  
   disclosed_quantity: 0,  
   trigger_price: 15,  
   is_amo: false,  
  };

  axios.post(url, data, { headers })  
   .then(response => {  
   console.log('Response:', response.data);  
   })  
   .catch(error => {  
   console.error('Error:', error.message);  
   });

  **Node.js Code:**

  **Node.js Code:**

  let UpstoxClient = require('upstox-js-sdk');  
  let defaultClient = UpstoxClient.ApiClient.instance;  
  var OAUTH2 = defaultClient.authentications['OAUTH2'];  
  OAUTH2.accessToken = "{your_access_token}";

  let apiInstance = new UpstoxClient.OrderApi();  
  let body = new UpstoxClient.PlaceOrderRequest(1, UpstoxClient.PlaceOrderRequest.ProductEnum.D, UpstoxClient.PlaceOrderRequest.ValidityEnum.DAY, 0.0, "NSE_EQ|INE528G01035",UpstoxClient.PlaceOrderRequest.OrderTypeEnum.SL_M,UpstoxClient.PlaceOrderRequest.TransactionTypeEnum.BUY, 0, 24.5, false);  
  let apiVersion = "2.0";

  apiInstance.placeOrder(body, apiVersion, (error, data, response) => {  
   if (error) {  
   console.error(error.response.text);  
   } else {  
   console.log('API called successfully. Returned data: ' + data);  
   }  
  });

## Place an intraday market order​

- Curl
- Python
- Node.js
- Java
- PHP
- Python SDK
- Node.js SDK
- Java SDK

  **Node.js Code:**

  **Node.js Code:**

  const axios = require('axios');

  const url = 'https://api.upstox.com/v2/order/place';  
  const headers = {  
   'Content-Type': 'application/json',  
   'Accept': 'application/json',  
   'Authorization': 'Bearer {your_access_token}',  
  };

  const data = {  
   quantity: 1,  
   product: 'I',  
   validity: 'DAY',  
   price: 0.0,  
   tag: 'string',  
   instrument_token: 'NSE_EQ|INE528G01035',  
   order_type: 'MARKET',  
   transaction_type: 'BUY',  
   disclosed_quantity: 0,  
   trigger_price: 0,  
   is_amo: false,  
  };

  axios.post(url, data, { headers })  
   .then(response => {  
   console.log('Response:', response.data);  
   })  
   .catch(error => {  
   console.error('Error:', error.message);  
   });

  **Node.js Code:**

  **Node.js Code:**

  let UpstoxClient = require('upstox-js-sdk');  
  let defaultClient = UpstoxClient.ApiClient.instance;  
  var OAUTH2 = defaultClient.authentications['OAUTH2'];  
  OAUTH2.accessToken = "{your_access_token}";

  let apiInstance = new UpstoxClient.OrderApi();  
  let body = new UpstoxClient.PlaceOrderRequest(1, UpstoxClient.PlaceOrderRequest.ProductEnum.I, UpstoxClient.PlaceOrderRequest.ValidityEnum.DAY, 0.0, "NSE_EQ|INE528G01035",UpstoxClient.PlaceOrderRequest.OrderTypeEnum.MARKET,UpstoxClient.PlaceOrderRequest.TransactionTypeEnum.BUY, 0, 0.0, false);  
  let apiVersion = "2.0";

  apiInstance.placeOrder(body, apiVersion, (error, data, response) => {  
   if (error) {  
   console.error(error.response.text);  
   } else {  
   console.log('API called successfully. Returned data: ' + data);  
   }  
  });

## Place an intraday limit order​

- Curl
- Python
- Node.js
- Java
- PHP
- Python SDK
- Node.js SDK
- Java SDK

  **Node.js Code:**

  **Node.js Code:**

  const axios = require('axios');

  const url = 'https://api.upstox.com/v2/order/place';  
  const headers = {  
   'Content-Type': 'application/json',  
   'Accept': 'application/json',  
   'Authorization': 'Bearer {your_access_token}',  
  };

  const data = {  
   quantity: 1,  
   product: 'I',  
   validity: 'DAY',  
   price: 20.0,  
   tag: 'string',  
   instrument_token: 'NSE_EQ|INE528G01035',  
   order_type: 'LIMIT',  
   transaction_type: 'BUY',  
   disclosed_quantity: 0,  
   trigger_price: 20.1,  
   is_amo: false,  
  };

  axios.post(url, data, { headers })  
   .then(response => {  
   console.log('Response:', response.data);  
   })  
   .catch(error => {  
   console.error('Error:', error.message);  
   });

  **Node.js Code:**

  **Node.js Code:**

  let UpstoxClient = require('upstox-js-sdk');  
  let defaultClient = UpstoxClient.ApiClient.instance;  
  var OAUTH2 = defaultClient.authentications['OAUTH2'];  
  OAUTH2.accessToken = "{your_access_token}";

  let apiInstance = new UpstoxClient.OrderApi();  
  let body = new UpstoxClient.PlaceOrderRequest(1, UpstoxClient.PlaceOrderRequest.ProductEnum.I, UpstoxClient.PlaceOrderRequest.ValidityEnum.DAY, 20.0, "NSE_EQ|INE528G01035",UpstoxClient.PlaceOrderRequest.OrderTypeEnum.LIMIT,UpstoxClient.PlaceOrderRequest.TransactionTypeEnum.BUY, 0, 20.1, false);  
  let apiVersion = "2.0";

  apiInstance.placeOrder(body, apiVersion, (error, data, response) => {  
   if (error) {  
   console.error(error.response.text);  
   } else {  
   console.log('API called successfully. Returned data: ' + data);  
   }  
  });

## Place an intraday stop-loss order​

- Curl
- Python
- Node.js
- Java
- PHP
- Python SDK
- Node.js SDK
- Java SDK

  **Node.js Code:**

  **Node.js Code:**

  const axios = require('axios');

  const url = 'https://api.upstox.com/v2/order/place';  
  const headers = {  
   'Content-Type': 'application/json',  
   'Accept': 'application/json',  
   'Authorization': 'Bearer {your_access_token}',  
  };

  const data = {  
   quantity: 1,  
   product: 'I',  
   validity: 'DAY',  
   price: 20.0,  
   tag: 'string',  
   instrument_token: 'NSE_EQ|INE528G01035',  
   order_type: 'SL',  
   transaction_type: 'BUY',  
   disclosed_quantity: 0,  
   trigger_price: 19.5,  
   is_amo: false,  
  };

  axios.post(url, data, { headers })  
   .then(response => {  
   console.log('Response:', response.data);  
   })  
   .catch(error => {  
   console.error('Error:', error.message);  
   });

  **Node.js Code:**

  **Node.js Code:**

  let UpstoxClient = require('upstox-js-sdk');  
  let defaultClient = UpstoxClient.ApiClient.instance;  
  var OAUTH2 = defaultClient.authentications['OAUTH2'];  
  OAUTH2.accessToken = "{your_access_token}";

  let apiInstance = new UpstoxClient.OrderApi();  
  let body = new UpstoxClient.PlaceOrderRequest(1, UpstoxClient.PlaceOrderRequest.ProductEnum.I, UpstoxClient.PlaceOrderRequest.ValidityEnum.DAY, 20.0, "NSE_EQ|INE528G01035",UpstoxClient.PlaceOrderRequest.OrderTypeEnum.SL,UpstoxClient.PlaceOrderRequest.TransactionTypeEnum.BUY, 0, 19.5, false);  
  let apiVersion = "2.0";

  apiInstance.placeOrder(body, apiVersion, (error, data, response) => {  
   if (error) {  
   console.error(error.response.text);  
   } else {  
   console.log('API called successfully. Returned data: ' + data);  
   }  
  });

## Place an intraday stop-loss market order​

- Curl
- Python
- Node.js
- Java
- PHP
- Python SDK
- Node.js SDK
- Java SDK

  **Node.js Code:**

  **Node.js Code:**

  const axios = require('axios');

  const url = 'https://api.upstox.com/v2/order/place';  
  const headers = {  
   'Content-Type': 'application/json',  
   'Accept': 'application/json',  
   'Authorization': 'Bearer {your_access_token}',  
  };

  const data = {  
   quantity: 1,  
   product: 'I',  
   validity: 'DAY',  
   price: 0.0,  
   tag: 'string',  
   instrument_token: 'NSE_EQ|INE528G01035',  
   order_type: 'SL-M',  
   transaction_type: 'BUY',  
   disclosed_quantity: 0,  
   trigger_price: 21.5,  
   is_amo: false,  
  };

  axios.post(url, data, { headers })  
   .then(response => {  
   console.log('Response:', response.data);  
   })  
   .catch(error => {  
   console.error('Error:', error.message);  
   });

  **Node.js Code:**

  **Node.js Code:**

  let UpstoxClient = require('upstox-js-sdk');  
  let defaultClient = UpstoxClient.ApiClient.instance;  
  var OAUTH2 = defaultClient.authentications['OAUTH2'];  
  OAUTH2.accessToken = "{your_access_token}";

  let apiInstance = new UpstoxClient.OrderApi();  
  let body = new UpstoxClient.PlaceOrderRequest(1, UpstoxClient.PlaceOrderRequest.ProductEnum.I, UpstoxClient.PlaceOrderRequest.ValidityEnum.DAY, 0.0, "NSE_EQ|INE528G01035",UpstoxClient.PlaceOrderRequest.OrderTypeEnum.SL_M,UpstoxClient.PlaceOrderRequest.TransactionTypeEnum.BUY, 0, 24.5, false);  
  let apiVersion = "2.0";

  apiInstance.placeOrder(body, apiVersion, (error, data, response) => {  
   if (error) {  
   console.error(error.response.text);  
   } else {  
   console.log('API called successfully. Returned data: ' + data);  
   }  
  });

## Place a delivery market amo (after market order)​

- Curl
- Python
- Node.js
- Java
- PHP
- Python SDK
- Node.js SDK
- Java SDK

  **Node.js Code:**

  **Node.js Code:**

  const axios = require('axios');

  const url = 'https://api.upstox.com/v2/order/place';  
  const headers = {  
   'Content-Type': 'application/json',  
   'Accept': 'application/json',  
   'Authorization': 'Bearer {your_access_token}',  
  };

  const data = {  
   quantity: 1,  
   product: 'D',  
   validity: 'DAY',  
   price: 0,  
   tag: 'string',  
   instrument_token: 'NSE_EQ|INE669E01016',  
   order_type: 'MARKET',  
   transaction_type: 'BUY',  
   disclosed_quantity: 0,  
   trigger_price: 0,  
   is_amo: true,  
  };

  axios.post(url, data, { headers })  
   .then(response => {  
   console.log('Response:', response.data);  
   })  
   .catch(error => {  
   console.error('Error:', error.message);  
   });

  **Node.js Code:**

  **Node.js Code:**

  let UpstoxClient = require('upstox-js-sdk');  
  let defaultClient = UpstoxClient.ApiClient.instance;  
  var OAUTH2 = defaultClient.authentications['OAUTH2'];  
  OAUTH2.accessToken = "{your_access_token}";

  let apiInstance = new UpstoxClient.OrderApi();  
  let body = new UpstoxClient.PlaceOrderRequest(1, UpstoxClient.PlaceOrderRequest.ProductEnum.D, UpstoxClient.PlaceOrderRequest.ValidityEnum.DAY, 0.0, "NSE_EQ|INE528G01035",UpstoxClient.PlaceOrderRequest.OrderTypeEnum.MARKET,UpstoxClient.PlaceOrderRequest.TransactionTypeEnum.BUY, 0, 0.0, true);  
  let apiVersion = "2.0";

  apiInstance.placeOrder(body, apiVersion, (error, data, response) => {  
   if (error) {  
   console.error(error.response.text);  
   } else {  
   console.log('API called successfully. Returned data: ' + data);  
   }  
  });

[PreviousBrokerage Details](/developer/api-documentation/example-code/charges/brokerage-details)[NextModify Order](/developer/api-documentation/example-code/orders/modify-order)

- Place a delivery market order
- Place a delivery limit order
- Place a delivery stop-loss order
- Place a delivery stop-loss order market
- Place an intraday market order
- Place an intraday limit order
- Place an intraday stop-loss order
- Place an intraday stop-loss market order
- Place a delivery market amo (after market order)

---

## [Convert Positions | Upstox Developer API](https://upstox.com/developer/api-documentation/example-code/portfolio/convert-positions)

- [](/developer/api-documentation/)
- [Example Code](/developer/api-documentation/example-code/introduction)
- Portfolio
- Convert Positions

On this page

# Convert Positions

## Convert a position from intraday to delivery​

- Curl
- Python
- Node.js
- Java
- PHP
- Python SDK
- Node.js SDK
- Java SDK

  **Node.js Code:**

  **Node.js Code:**

  const axios = require('axios');

  const url = 'https://api.upstox.com/v2/portfolio/convert-position';  
  const headers = {  
   'Content-Type': 'application/json',  
   'Accept': 'application/json',  
   'Authorization': 'Bearer {your_access_token}', // Replace {your_access_token} with your actual access token  
  };

  const data = {  
   "instrument_token": "NSE_EQ|INE528G01035",  
   "new_product": "D",  
   "old_product": "I",  
   "transaction_type": "BUY",  
   "quantity": 1  
  };

  axios.put(url, data, { headers })  
   .then(response => {  
   console.log('Status Code:', response.status);  
   console.log('Response Data:', response.data);  
   })  
   .catch(error => {  
   console.error('Error:', error.message);  
   });

  **Node.js Code:**

  **Node.js Code:**

  let UpstoxClient = require('upstox-js-sdk');  
  let defaultClient = UpstoxClient.ApiClient.instance;

  // Configure OAuth2 access token for authorization: OAUTH2  
  let OAUTH2 = defaultClient.authentications['OAUTH2'];  
  OAUTH2.accessToken = '{your_access_token}';

  let apiInstance = new UpstoxClient.PortfolioApi();  
  let body = new UpstoxClient.ConvertPositionRequest("NSE_EQ|INE528G01035",UpstoxClient.ConvertPositionRequest.NewProductEnum.D,UpstoxClient.ConvertPositionRequest.OldProductEnum.I,UpstoxClient.ConvertPositionRequest.TransactionTypeEnum.BUY,1); // ConvertPositionRequest |  
  let apiVersion = "2.0"; // String | API Version Header

  apiInstance.convertPositions(body, apiVersion, (error, data, response) => {  
   if (error) {  
   console.error(error);  
   } else {  
   console.log('API called successfully. Returned data: ' + JSON.stringify(data));  
   }  
  });

## Convert a position from delivery to intraday​

- Curl
- Python
- Node.js
- Java
- PHP
- Python SDK
- Node.js SDK
- Java SDK

  **Node.js Code:**

  **Node.js Code:**

  const axios = require('axios');

  const url = 'https://api.upstox.com/v2/portfolio/convert-position';  
  const headers = {  
   'Content-Type': 'application/json',  
   'Accept': 'application/json',  
   'Authorization': 'Bearer {your_access_token}', // Replace {your_access_token} with your actual access token  
  };

  const data = {  
   "instrument_token": "NSE_EQ|INE528G01035",  
   "new_product": "I",  
   "old_product": "D",  
   "transaction_type": "BUY",  
   "quantity": 1  
  };

  axios.put(url, data, { headers })  
   .then(response => {  
   console.log('Status Code:', response.status);  
   console.log('Response Data:', response.data);  
   })  
   .catch(error => {  
   console.error('Error:', error.message);  
   });

  **Node.js Code:**

  **Node.js Code:**

  let UpstoxClient = require('upstox-js-sdk');  
  let defaultClient = UpstoxClient.ApiClient.instance;

  // Configure OAuth2 access token for authorization: OAUTH2  
  let OAUTH2 = defaultClient.authentications['OAUTH2'];  
  OAUTH2.accessToken = '{your_access_token}';

  let apiInstance = new UpstoxClient.PortfolioApi();  
  let body = new UpstoxClient.ConvertPositionRequest("NSE_EQ|INE528G01035",UpstoxClient.ConvertPositionRequest.NewProductEnum.I,UpstoxClient.ConvertPositionRequest.OldProductEnum.D,UpstoxClient.ConvertPositionRequest.TransactionTypeEnum.BUY,1); // ConvertPositionRequest |  
  let apiVersion = "2.0"; // String | API Version Header

  apiInstance.convertPositions(body, apiVersion, (error, data, response) => {  
   if (error) {  
   console.error(error);  
   } else {  
   console.log('API called successfully. Returned data: ' + JSON.stringify(data));  
   }  
  });

[PreviousGet Trade History](/developer/api-documentation/example-code/orders/get-historical-trades)[NextGet Holdings](/developer/api-documentation/example-code/portfolio/get-holdings)

- Convert a position from intraday to delivery
- Convert a position from delivery to intraday

---

## [Get Report Meta Data | Upstox Developer API](https://upstox.com/developer/api-documentation/example-code/trade-profit-and-loss/get-report-meta-data)

- [](/developer/api-documentation/)
- [Example Code](/developer/api-documentation/example-code/introduction)
- Trade Profit and Loss
- Get Report Meta Data

On this page

# Get Report Meta Data

## Get report meta data for equity segment​

- Curl
- Python
- Node.js
- Java
- PHP
- Python SDK
- Node.js SDK
- Java SDK

  **Node.js Code:**

  **Node.js Code:**

  const axios = require('axios');

  const url = 'https://api.upstox.com/v2/trade/profit-loss/metadata';  
  const headers = {  
   'Accept': 'application/json',  
   'Authorization': 'Bearer {your_access_token}'  
  };

  const params = {  
   'from_date': '05-11-2023',  
   'to_date': '19-12-2023',  
   'segment': 'EQ',  
   'financial_year': '2324'  
  };

  axios.get(url, { headers, params })  
   .then(response => {  
   console.log(response.status);  
   console.log(response.data);  
   })  
   .catch(error => {  
   console.error('Error:', error.message || error);  
   });

  **Node.js Code:**

  **Node.js Code:**

  let UpstoxClient = require('upstox-js-sdk');  
  let defaultClient = UpstoxClient.ApiClient.instance;

  // Configure OAuth2 access token for authorization: OAUTH2  
  let OAUTH2 = defaultClient.authentications['OAUTH2'];  
  OAUTH2.accessToken = '{your_access_token}';

  let apiInstance = new UpstoxClient.TradeProfitAndLossApi();  
  let segment = "EQ"; // String | Segment for which data is requested can be from the following options EQ - Equity, FO - Futures and Options, COM - Commodity, CD - Currency Derivatives  
  let financialYear = "2324"; // String | Financial year for which data has been requested. Concatenation of last 2 digits of from year and to year Sample:for 2021-2022, financial_year will be 2122  
  let apiVersion = "2.0"; // String | API Version Header  
  let opts = {  
   'fromDate': "02-04-2023", // String | Date from which data needs to be fetched. from_date and to_date should fall under the same financial year as mentioned in financial_year attribute. Date in dd-mm-yyyy format  
   'toDate': "20-03-2024" // String | Date till which data needs to be fetched. from_date and to_date should fall under the same financial year as mentioned in financial_year attribute. Date in dd-mm-yyyy format  
  };  
  apiInstance.getTradeWiseProfitAndLossMetaData(segment, financialYear, apiVersion, opts, (error, data, response) => {  
   if (error) {  
   console.error(error);  
   } else {  
   console.log('API called successfully. Returned data: ' + JSON.stringify(data));  
   }  
  });

## Get report meta data for futures and options segment​

- Curl
- Python
- Node.js
- Java
- PHP
- Python SDK
- Node.js SDK
- Java SDK

  **Node.js Code:**

  **Node.js Code:**

  const axios = require('axios');

  const url = 'https://api.upstox.com/v2/trade/profit-loss/metadata';  
  const headers = {  
   'Accept': 'application/json',  
   'Authorization': 'Bearer {your_access_token}'  
  };

  const params = {  
   'from_date': '05-11-2023',  
   'to_date': '19-12-2023',  
   'segment': 'FO',  
   'financial_year': '2324'  
  };

  axios.get(url, { headers, params })  
   .then(response => {  
   console.log(response.status);  
   console.log(response.data);  
   })  
   .catch(error => {  
   console.error('Error:', error.message || error);  
   });

  **Node.js Code:**

  **Node.js Code:**

  let UpstoxClient = require('upstox-js-sdk');  
  let defaultClient = UpstoxClient.ApiClient.instance;

  // Configure OAuth2 access token for authorization: OAUTH2  
  let OAUTH2 = defaultClient.authentications['OAUTH2'];  
  OAUTH2.accessToken = '{your_access_token}';

  let apiInstance = new UpstoxClient.TradeProfitAndLossApi();  
  let segment = "FO"; // String | Segment for which data is requested can be from the following options EQ - Equity, FO - Futures and Options, COM - Commodity, CD - Currency Derivatives  
  let financialYear = "2324"; // String | Financial year for which data has been requested. Concatenation of last 2 digits of from year and to year Sample:for 2021-2022, financial_year will be 2122  
  let apiVersion = "2.0"; // String | API Version Header  
  let opts = {  
   'fromDate': "02-04-2023", // String | Date from which data needs to be fetched. from_date and to_date should fall under the same financial year as mentioned in financial_year attribute. Date in dd-mm-yyyy format  
   'toDate': "20-03-2024" // String | Date till which data needs to be fetched. from_date and to_date should fall under the same financial year as mentioned in financial_year attribute. Date in dd-mm-yyyy format  
  };  
  apiInstance.getTradeWiseProfitAndLossMetaData(segment, financialYear, apiVersion, opts, (error, data, response) => {  
   if (error) {  
   console.error(error);  
   } else {  
   console.log('API called successfully. Returned data: ' + JSON.stringify(data));  
   }  
  });

[PreviousGet Positions](/developer/api-documentation/example-code/portfolio/get-positions)[NextGet Profit Loss Report](/developer/api-documentation/example-code/trade-profit-and-loss/get-profit-loss-report)

- Get report meta data for equity segment
- Get report meta data for futures and options segment

---

## [Historical Candle Data | Upstox Developer API](https://upstox.com/developer/api-documentation/example-code/historical-data/historical-candle-data)

- [](/developer/api-documentation/)
- [Example Code](/developer/api-documentation/example-code/introduction)
- Historical Data
- Historical Candle Data

On this page

# Historical Candle Data

## Get historical candle data with a 1-minute interval​

- Curl
- Python
- Node.js
- Java
- PHP
- Python SDK
- Node.js SDK
- Java SDK

  **Node.js Code:**

  **Node.js Code:**

  const axios = require('axios');

  const url = 'https://api.upstox.com/v2/historical-candle/NSE_EQ%7CINE848E01016/1minute/2023-11-13/2023-11-12';  
  const headers = {  
   'Accept': 'application/json'  
  };

  axios.get(url, { headers })  
   .then(response => {  
   // Do something with the response data (e.g., print it)  
   console.log(response.data);  
   })  
   .catch(error => {  
   // Print an error message if the request was not successful  
   console.error(`Error: ${error.response.status} - ${error.response.data}`);  
   });

  **Node.js Code:**

  **Node.js Code:**

  let UpstoxClient = require('upstox-js-sdk');  
  let apiInstance = new UpstoxClient.HistoryApi();

  let apiVersion = "2.0";  
  let instrumentKey = "NSE_EQ|INE669E01016";  
  let interval = "1minute";  
  let toDate = "2023-11-13";  
  let fromDate = "2023-11-12";

  apiInstance.getHistoricalCandleData1(instrumentKey, interval, toDate, fromDate,apiVersion, (error, data, response) => {  
   if (error) {  
   console.error(error);  
   } else {  
   console.log('API called successfully. Returned data: ' + JSON.stringify(data));  
   }  
  });

## Get data with a 30-minute interval​

- Curl
- Python
- Node.js
- Java
- PHP
- Python SDK
- Node.js SDK
- Java SDK

  **Node.js Code:**

  **Node.js Code:**

  const axios = require('axios');

  const url = 'https://api.upstox.com/v2/historical-candle/NSE_EQ%7CINE848E01016/30minute/2023-11-13/2023-11-12';  
  const headers = {  
   'Accept': 'application/json'  
  };

  axios.get(url, { headers })  
   .then(response => {  
   // Do something with the response data (e.g., print it)  
   console.log(response.data);  
   })  
   .catch(error => {  
   // Print an error message if the request was not successful  
   console.error(`Error: ${error.response.status} - ${error.response.data}`);  
   });

  **Node.js Code:**

  **Node.js Code:**

  let UpstoxClient = require('upstox-js-sdk');  
  let apiInstance = new UpstoxClient.HistoryApi();

  let apiVersion = "2.0";  
  let instrumentKey = "NSE_EQ|INE669E01016";  
  let interval = "30minute";  
  let toDate = "2023-11-13";  
  let fromDate = "2023-11-12";  
  apiInstance.getHistoricalCandleData1(instrumentKey, interval, toDate, fromDate,apiVersion, (error, data, response) => {  
   if (error) {  
   console.error(error);  
   } else {  
   console.log('API called successfully. Returned data: ' + JSON.stringify(data));  
   }  
  });

## Get data with a daily interval​

- Curl
- Python
- Node.js
- Java
- PHP
- Python SDK
- Node.js SDK
- Java SDK

  **Node.js Code:**

  **Node.js Code:**

  const axios = require('axios');

  const url = 'https://api.upstox.com/v2/historical-candle/NSE_EQ%7CINE848E01016/day/2023-11-19/2023-11-12';  
  const headers = {  
   'Accept': 'application/json'  
  };

  axios.get(url, { headers })  
   .then(response => {  
   // Do something with the response data (e.g., print it)  
   console.log(response.data);  
   })  
   .catch(error => {  
   // Print an error message if the request was not successful  
   console.error(`Error: ${error.response.status} - ${error.response.data}`);  
   });

## Get data with a weekly interval​

- Curl
- Python
- Node.js
- Java
- PHP
- Python SDK
- Node.js SDK
- Java SDK

  **Node.js Code:**

  **Node.js Code:**

  const axios = require('axios');

  const url = 'https://api.upstox.com/v2/historical-candle/NSE_EQ%7CINE848E01016/week/2023-11-19/2023-07-12';  
  const headers = {  
   'Accept': 'application/json'  
  };

  axios.get(url, { headers })  
   .then(response => {  
   // Do something with the response data (e.g., print it)  
   console.log(response.data);  
   })  
   .catch(error => {  
   // Print an error message if the request was not successful  
   console.error(`Error: ${error.response.status} - ${error.response.data}`);  
   });

## Get data with a monthly interval​

- Curl
- Python
- Node.js
- Java
- PHP
- Python SDK
- Node.js SDK
- Java SDK

  **Node.js Code:**

  **Node.js Code:**

  const axios = require('axios');

  const url = 'https://api.upstox.com/v2/historical-candle/NSE_EQ%7CINE848E01016/month/2023-11-19/2022-11-12';  
  const headers = {  
   'Accept': 'application/json'  
  };

  axios.get(url, { headers })  
   .then(response => {  
   // Do something with the response data (e.g., print it)  
   console.log(response.data);  
   })  
   .catch(error => {  
   // Print an error message if the request was not successful  
   console.error(`Error: ${error.response.status} - ${error.response.data}`);  
   });

## Get historical candle data with a 1-minute interval​

- Curl
- Python
- Node.js
- Java
- PHP
- Python SDK
- Node.js SDK
- Java SDK

  **Node.js Code:**

  **Node.js Code:**

  const axios = require('axios');

  const url = 'https://api.upstox.com/v2/historical-candle/NSE_EQ%7CINE848E01016/1minute/2023-11-13';  
  const headers = {  
   'Accept': 'application/json'  
  };

  axios.get(url, { headers })  
   .then(response => {  
   // Do something with the response data (e.g., print it)  
   console.log(response.data);  
   })  
   .catch(error => {  
   // Print an error message if the request was not successful  
   console.error(`Error: ${error.response.status} - ${error.response.data}`);  
   });

  **Node.js Code:**

  **Node.js Code:**

  let UpstoxClient = require('upstox-js-sdk');  
  let apiInstance = new UpstoxClient.HistoryApi();

  let apiVersion = "2.0";  
  let instrumentKey = "NSE_EQ|INE669E01016";  
  let interval = "1minute";  
  let toDate = "2023-11-13";  
  apiInstance.getHistoricalCandleData(instrumentKey, interval, toDate, apiVersion, (error, data, response) => {  
   if (error) {  
   console.error(error);  
   } else {  
   console.log('API called successfully. Returned data: ' + JSON.stringify(data));  
   }  
  });

## Get data with a 30-minute interval​

- Curl
- Python
- Node.js
- Java
- PHP
- Python SDK
- Node.js SDK
- Java SDK

  **Node.js Code:**

  **Node.js Code:**

  const axios = require('axios');

  const url = 'https://api.upstox.com/v2/historical-candle/NSE_EQ%7CINE848E01016/30minute/2023-11-13';  
  const headers = {  
   'Accept': 'application/json'  
  };

  axios.get(url, { headers })  
   .then(response => {  
   // Do something with the response data (e.g., print it)  
   console.log(response.data);  
   })  
   .catch(error => {  
   // Print an error message if the request was not successful  
   console.error(`Error: ${error.response.status} - ${error.response.data}`);  
   });

  **Node.js Code:**

  **Node.js Code:**

  let UpstoxClient = require('upstox-js-sdk');  
  let apiInstance = new UpstoxClient.HistoryApi();

  let apiVersion = "2.0";  
  let instrumentKey = "NSE_EQ|INE669E01016";  
  let interval = "30minute";  
  let toDate = "2023-11-13";

  apiInstance.getHistoricalCandleData(instrumentKey, interval, toDate, apiVersion, (error, data, response) => {  
   if (error) {  
   console.error(error);  
   } else {  
   console.log('API called successfully. Returned data: ' + JSON.stringify(data));  
   }  
  });

## Get data with a daily interval​

- Curl
- Python
- Node.js
- Java
- PHP
- Python SDK
- Node.js SDK
- Java SDK

  **Node.js Code:**

  **Node.js Code:**

  const axios = require('axios');

  const url = 'https://api.upstox.com/v2/historical-candle/NSE_EQ%7CINE848E01016/day/2023-11-19';  
  const headers = {  
   'Accept': 'application/json'  
  };

  axios.get(url, { headers })  
   .then(response => {  
   // Do something with the response data (e.g., print it)  
   console.log(response.data);  
   })  
   .catch(error => {  
   // Print an error message if the request was not successful  
   console.error(`Error: ${error.response.status} - ${error.response.data}`);  
   });

## Get data with a weekly interval​

- Curl
- Python
- Node.js
- Java
- PHP
- Python SDK
- Node.js SDK
- Java SDK

  **Node.js Code:**

  **Node.js Code:**

  const axios = require('axios');

  const url = 'https://api.upstox.com/v2/historical-candle/NSE_EQ%7CINE848E01016/week/2023-11-19';  
  const headers = {  
   'Accept': 'application/json'  
  };

  axios.get(url, { headers })  
   .then(response => {  
   // Do something with the response data (e.g., print it)  
   console.log(response.data);  
   })  
   .catch(error => {  
   // Print an error message if the request was not successful  
   console.error(`Error: ${error.response.status} - ${error.response.data}`);  
   });

## Get data with a monthly interval​

- Curl
- Python
- Node.js
- Java
- PHP
- Python SDK
- Node.js SDK
- Java SDK

  **Node.js Code:**

  **Node.js Code:**

  const axios = require('axios');

  const url = 'https://api.upstox.com/v2/historical-candle/NSE_EQ%7CINE848E01016/month/2023-11-19';  
  const headers = {  
   'Accept': 'application/json'  
  };

  axios.get(url, { headers })  
   .then(response => {  
   // Do something with the response data (e.g., print it)  
   console.log(response.data);  
   })  
   .catch(error => {  
   // Print an error message if the request was not successful  
   console.error(`Error: ${error.response.status} - ${error.response.data}`);  
   });

[PreviousGet Trade Charges](/developer/api-documentation/example-code/trade-profit-and-loss/get-trade-charges)[NextIntraday Candle Data](/developer/api-documentation/example-code/historical-data/intra-day-candle-data)

- Get historical candle data with a 1-minute interval
- Get data with a 30-minute interval
- Get data with a daily interval
- Get data with a weekly interval
- Get data with a monthly interval
- Get historical candle data with a 1-minute interval
- Get data with a 30-minute interval
- Get data with a daily interval
- Get data with a weekly interval
- Get data with a monthly interval

---

## [Full Market Quotes | Upstox Developer API](https://upstox.com/developer/api-documentation/example-code/market-quote/full-market-quotes)

- [](/developer/api-documentation/)
- [Example Code](/developer/api-documentation/example-code/introduction)
- Market Quote
- Full Market Quotes

On this page

# Full Market Quotes

## Get full market quote​

- Curl
- Python
- Node.js
- Java
- PHP
- Python SDK
- Node.js SDK
- Java SDK

  **Node.js Code:**

  **Node.js Code:**

  const axios = require('axios');

  const url = 'https://api.upstox.com/v2/market-quote/quotes?instrument_key=NSE_EQ%7CINE848E01016';  
  const headers = {  
   'Accept': 'application/json',  
   'Authorization': 'Bearer {your_access_token}'  
  };

  axios.get(url, { headers })  
   .then(response => {  
   console.log(response.data);  
   })  
   .catch(error => {  
   console.error(error);  
   });

  **Node.js Code:**

  **Node.js Code:**

  let UpstoxClient = require('upstox-js-sdk');  
  let defaultClient = UpstoxClient.ApiClient.instance;  
  var OAUTH2 = defaultClient.authentications['OAUTH2'];  
  OAUTH2.accessToken = "{your_access_token}";  
  let apiInstance = new UpstoxClient.MarketQuoteApi();

  let apiVersion = "2.0";  
  let symbol = "NSE_EQ|INE669E01016";

  apiInstance.getFullMarketQuote(symbol, apiVersion, (error, data, response) => {  
   if (error) {  
   console.error(error);  
   } else {  
   console.log('API called successfully. Returned data: ' + JSON.stringify(data));  
   }  
  });

## Get full market quote for multiple instrument keys​

- Curl
- Python
- Node.js
- Java
- PHP
- Python SDK
- Node.js SDK
- Java SDK

  **Node.js Code:**

  **Node.js Code:**

  const axios = require('axios');

  const url = 'https://api.upstox.com/v2/market-quote/quotes?instrument_key=NSE_EQ%7CINE848E01016,NSE_EQ|INE669E01016';  
  const headers = {  
   'Accept': 'application/json',  
   'Authorization': 'Bearer {your_access_token}'  
  };

  axios.get(url, { headers })  
   .then(response => {  
   console.log(response.data);  
   })  
   .catch(error => {  
   console.error(error);  
   });

  **Node.js Code:**

  **Node.js Code:**

  let UpstoxClient = require('upstox-js-sdk');  
  let defaultClient = UpstoxClient.ApiClient.instance;  
  var OAUTH2 = defaultClient.authentications['OAUTH2'];  
  OAUTH2.accessToken = "{your_access_token}";  
  let apiInstance = new UpstoxClient.MarketQuoteApi();

  let apiVersion = "2.0";  
  let symbol = "NSE_EQ|INE669E01016,NSE_EQ|INE848E01016";

  apiInstance.getFullMarketQuote(symbol, apiVersion, (error, data, response) => {  
   if (error) {  
   console.error(error);  
   } else {  
   console.log('API called successfully. Returned data: ' + JSON.stringify(data));  
   }  
  });

[PreviousIntraday Candle Data](/developer/api-documentation/example-code/historical-data/intra-day-candle-data)[NextLTP Market Quotes](/developer/api-documentation/example-code/market-quote/ltp-quotes)

- Get full market quote
- Get full market quote for multiple instrument keys

---

## [Market Holidays | Upstox Developer API](https://upstox.com/developer/api-documentation/example-code/market-information/market-holidays)

- [](/developer/api-documentation/)
- [Example Code](/developer/api-documentation/example-code/introduction)
- Market Information
- Market Holidays

On this page

# Market Holidays

## Get market holidays for current year​

- Curl
- Python
- Node.js
- Java
- PHP
- **Node.js Code:**

  **Node.js Code:**

  const axios = require('axios');

  const url = 'https://api.upstox.com/v2/market/holidays';  
  const headers = {  
   'Accept': 'application/json'  
  };

  axios.get(url, { headers })  
   .then(response => {  
   // Process the JSON response  
   console.log(response.data);  
   })  
   .catch(error => {  
   console.error('Error:', error);  
   });

## Get market holiday status of a date​

- Curl
- Python
- Node.js
- Java
- PHP
- **Node.js Code:**

  **Node.js Code:**

  const axios = require('axios');

  const url = 'https://api.upstox.com/v2/market/holidays/2024-01-22';  
  const headers = {  
   'Accept': 'application/json'  
  };

  axios.get(url, { headers })  
   .then(response => {  
   // Process the JSON response  
   console.log(response.data);  
   })  
   .catch(error => {  
   console.error('Error:', error);  
   });

[PreviousOHLC Market Quotes](/developer/api-documentation/example-code/market-quote/ohlc-quotes)[NextMarket Timings](/developer/api-documentation/example-code/market-information/market-timings)

- Get market holidays for current year
- Get market holiday status of a date

---

## [Option Contracts | Upstox Developer API](https://upstox.com/developer/api-documentation/example-code/option-chain/option-contracts)

- [](/developer/api-documentation/)
- [Example Code](/developer/api-documentation/example-code/introduction)
- Option Chain
- Option Contracts

On this page

# Option Contracts

## Get option contracts of an instrument key​

- Curl
- Python
- Node.js
- Java
- PHP
- **Node.js Code:**

  **Node.js Code:**

  const axios = require('axios');

  const url = 'https://api.upstox.com/v2/option/contract?instrument_key=NSE_INDEX%7CNifty%2050';  
  const headers = {  
   'Accept': 'application/json',  
   'Authorization': 'Bearer {your_access_token}'  
  };

  axios.get(url, { headers })  
   .then(response => {  
   console.log(response.data);  
   })  
   .catch(error => {  
   console.error('Error:', error);  
   });

## Get option contracts of an instrument key with expiry date​

- Curl
- Python
- Node.js
- Java
- PHP
- **Node.js Code:**

  **Node.js Code:**

  const axios = require('axios');

  const url = 'https://api.upstox.com/v2/option/contract?instrument_key=NSE_INDEX%7CNifty%2050&expiry_date=2024-03-28';  
  const headers = {  
   'Accept': 'application/json',  
   'Authorization': 'Bearer {your_access_token}'  
  };

  axios.get(url, { headers })  
   .then(response => {  
   console.log(response.data);  
   })  
   .catch(error => {  
   console.error('Error:', error);  
   });

[PreviousExchange Status](/developer/api-documentation/example-code/market-information/exchange-status)[NextPut/Call Option Chain](/developer/api-documentation/example-code/option-chain/put-call-option-chain)

- Get option contracts of an instrument key
- Get option contracts of an instrument key with expiry date

---

## [Announcements | Upstox Developer API](https://upstox.com/developer/api-documentation/announcements#docusaurus_skipToContent_fallback)

On this page

# Announcements

This section is dedicated to providing you with the most recent updates and essential information.

## Active Announcements​

- **Apr 25, 2024: CSV Instruments File Deprecation Notice**  
  The [CSV format](/developer/api-documentation/instruments#csv-files) for the instruments file will soon be deprecated. We recommend users to transition to the [JSON version](/developer/api-documentation/instruments#json-files) for improved functionality and support.  
  [Read more](/developer/api-documentation/announcements/instruments-csv-deprecation-notice)

- **Mar 7, 2024: New URL and Simplified Headers**  
  Upstox API now accessible at a new URL <https://api.upstox.com/v2> with simplified header requirements. Old and new URLs operational during transition. Migration advised.  
  [Read more](/developer/api-documentation/announcements/new-url-and-simplified-headers)

Remember to check back regularly for the latest news and updates.

- Active Announcements

---

## [Announcements | Upstox Developer API](https://upstox.com/developer/api-documentation/announcements#active-announcements)

On this page

# Announcements

This section is dedicated to providing you with the most recent updates and essential information.

## Active Announcements​

- **Apr 25, 2024: CSV Instruments File Deprecation Notice**  
  The [CSV format](/developer/api-documentation/instruments#csv-files) for the instruments file will soon be deprecated. We recommend users to transition to the [JSON version](/developer/api-documentation/instruments#json-files) for improved functionality and support.  
  [Read more](/developer/api-documentation/announcements/instruments-csv-deprecation-notice)

- **Mar 7, 2024: New URL and Simplified Headers**  
  Upstox API now accessible at a new URL <https://api.upstox.com/v2> with simplified header requirements. Old and new URLs operational during transition. Migration advised.  
  [Read more](/developer/api-documentation/announcements/new-url-and-simplified-headers)

Remember to check back regularly for the latest news and updates.

- Active Announcements

---

## [Instruments | Upstox Developer API](https://upstox.com/developer/api-documentation/instruments#csv-files)

- [](/developer/api-documentation/)
- [Developer API](/developer/api-documentation/open-api)
- Instruments

On this page

# Instruments

Note

- **The CSV format for instruments files is being deprecated.** Switch to the JSON format for improved performance. Details at [CSV Instruments File Deprecation Notice](/developer/api-documentation/announcements/instruments-csv-deprecation-notice).
- The list of suspended instruments is available in the [JSON section](/developer/api-documentation/instruments#json-files) below.

Recommendations

- Use for uniquely identifying instruments, as it remains unique for each instrument. Conversely, may be reused by the exchange for a different instrument after its expiry.
- Use Instruments data in JSON format instead of CSV, as its structure has been designed for enhanced robustness and future scalability, making programmatic processing easier.

## CSV Files​

These URLs provide access to the complete list of BOD contracts available for trading on Upstox in CSV format.

- [Complete](https://assets.upstox.com/market-quote/instruments/exchange/complete.csv.gz)
- [NSE](https://assets.upstox.com/market-quote/instruments/exchange/NSE.csv.gz)
- [BSE](https://assets.upstox.com/market-quote/instruments/exchange/BSE.csv.gz)
- [MCX](https://assets.upstox.com/market-quote/instruments/exchange/MCX.csv.gz)

### Sample CSV Record​

| instrument_key | exchange_token | tradingsymbol | name                | last_price              | expiry | strike     | tick_size | lot_size | instrument_type | option_type | exchange |
| -------------- | -------------- | ------------- | ------------------- | ----------------------- | ------ | ---------- | --------- | -------- | --------------- | ----------- | -------- | ------ |
| NSE_FO         | 164693         | 164693        | RELIANCE24JAN1840CE | RELIANCE INDUSTRIES LTD | 424.8  | 2024-01-25 | 1840.0    | 0.05     | 250             | OPTSTK      | CE       | NSE_FO |

### Field Description​

| Name            | Type   | Description                                                                                                                                                                                                                                                          |
| --------------- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| instrument_key  | string | The unique identifier used across Upstox APIs for instrument identification. For the regex pattern applicable to this field, see the [Field Pattern Appendix](/developer/api-documentation/appendix/field-pattern).                                                  |
| exchange_token  | number | The numerical identifier issued by the exchange representing the instrument.                                                                                                                                                                                         |
| tradingsymbol   | string | Shows the trading symbol which could be a combination of symbol name, instrument, expiry date etc. The format of this value may vary between weekly and monthly contracts, leading to inconsistencies. These inconsistencies have been resolved in the JSON version. |
| name            | string | Name of the company (for equity instruments).                                                                                                                                                                                                                        |
| last_price      | number | Last traded price.                                                                                                                                                                                                                                                   |
| expiry          | string | Expiry date (for derivatives). Data format is                                                                                                                                                                                                                        |
| strike          | number | Indicates the predetermined price at which an option can be bought or sold when it's exercised.                                                                                                                                                                      |
| tick_size       | number | Measure of the minimum upward or downward movement in the price of an instrument.                                                                                                                                                                                    |
| lot_size        | number | Minimum size in which the stock futures or index futures can be traded.                                                                                                                                                                                              |
| instrument_type | string | Instrument type of a particular contract.                                                                                                                                                                                                                            |

Possible values: , , etc.  
option_type| string| Option type of the option contracts (applicable only for options contract).  
Possible values: ,  
exchange| string| Exchange to which the order is associated.  
Possible values: , , , , , etc.

## JSON files​

These URLs provide access to the complete list of BOD contracts available for trading on Upstox in JSON format.

- [Complete](https://assets.upstox.com/market-quote/instruments/exchange/complete.json.gz)
- [NSE](https://assets.upstox.com/market-quote/instruments/exchange/NSE.json.gz)
- [BSE](https://assets.upstox.com/market-quote/instruments/exchange/BSE.json.gz)
- [MCX](https://assets.upstox.com/market-quote/instruments/exchange/MCX.json.gz)
- [Suspended](https://assets.upstox.com/market-quote/instruments/exchange/suspended-instrument.json.gz)

### Sample JSON Object​

- EQ
- Futures
- Options
- INDEX

Note

- When you're searching for instrument keys within an instrument JSON file, you can employ the and parameters to refine and narrow down the list of instrument keys. For instance, if you're looking for the instrument key for Reliance Equity, specify the as and the as , excluding other segments and instrument types from your search criteria.

### Field Description

| Field Name | Type   | Description                                    |
| ---------- | ------ | ---------------------------------------------- |
| segment    | string | Segment to which the instrument is associated. |

Possible values: , , , , , , , ,  
name| string| The name of the equity.  
exchange| string| Exchange to which the instrument is associated.  
Possible values: , ,  
isin| string| The International Securities Identification Number.  
instrument_type| string| The instrument types for NSE are present at [NSE India](https://www.nseindia.com/market-data/legend-of-series) and for BSE are present at [BSE India](https://www.bseindia.com/markets/equity/EQReports/tra_trading.aspx).  
instrument_key| string| The unique identifier used across Upstox APIs for instrument identification. For the regex pattern applicable to this field, see the [Field Pattern Appendix](/developer/api-documentation/appendix/field-pattern).  
lot_size| number| The size of one lot of the equity.  
freeze_quantity| number| The maximum quantity that can be frozen.  
exchange_token| string| The exchange-specific token for the equity.  
tick_size| number| The minimum price movement of the equity.  
trading_symbol| string| Trading symbol of the instrument.  
short_name| string| A shorter or abbreviated name of the equity.  
security_type| string| Identifies the classification or status of a security within the market. Valid security types can be found in the [Security Type Appendix](/developer/api-documentation/appendix/equity-security-type)

Note

- When you're searching for instrument keys within an instrument JSON file, you can employ the and parameters to refine and narrow down the list of instrument keys. For instance, if you're looking for the instrument key for Reliance Future, specify the as and the as , excluding other segments and instrument types from your search criteria.

### Field Description

| Field Name        | Type    | Description                                                                                                                                                                                                         |
| ----------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| weekly            | boolean | Indicates if the future is weekly.                                                                                                                                                                                  |
| segment           | string  | Segment to which the instrument is associated. Possible values: , , , , , , , ,                                                                                                                                     |
| name              | string  | The name of the future.                                                                                                                                                                                             |
| exchange          | string  | Exchange to which the instrument is associated. Possible values: , ,                                                                                                                                                |
| expiry            | date    | The expiry date of the future.                                                                                                                                                                                      |
| instrument_type   | string  | The type of the future instrument. Possible values:                                                                                                                                                                 |
| underlying_symbol | string  | The symbol of the underlying asset.                                                                                                                                                                                 |
| instrument_key    | string  | The unique identifier used across Upstox APIs for instrument identification. For the regex pattern applicable to this field, see the [Field Pattern Appendix](/developer/api-documentation/appendix/field-pattern). |
| lot_size          | number  | The size of one lot of the future.                                                                                                                                                                                  |
| freeze_quantity   | number  | The maximum quantity that can be frozen.                                                                                                                                                                            |
| exchange_token    | string  | The exchange-specific token for the future.                                                                                                                                                                         |
| minimum_lot       | number  | The minimum lot size for the future.                                                                                                                                                                                |
| underlying_key    | string  | The for the underlying asset.                                                                                                                                                                                       |
| tick_size         | number  | The minimum price movement of the future.                                                                                                                                                                           |
| underlying_type   | string  | The type of the underlying asset. Possible values: , , , ,                                                                                                                                                          |
| trading_symbol    | string  | The symbol used for trading the future. Format:                                                                                                                                                                     |

Note

- When you're searching for instrument keys within an instrument JSON file, you can employ the and parameters to refine and narrow down the list of instrument keys. For instance, if you're looking for the instrument key for Reliance Call Option, specify the as and the as , excluding other segments and instrument types from your search criteria. If you want to search for Put Option then set as .

### Field Description

| Field Name        | Type    | Description                                                                                                                                                                                                         |
| ----------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| weekly            | boolean | Indicates if the option is weekly.                                                                                                                                                                                  |
| segment           | string  | The market segment of the option. Possible values: , , , , , , , ,                                                                                                                                                  |
| name              | string  | The name of the option.                                                                                                                                                                                             |
| exchange          | string  | Exchange to which the instrument is associated. Possible values: , ,                                                                                                                                                |
| expiry            | date    | The expiry date of the option.                                                                                                                                                                                      |
| instrument_type   | string  | The type of the option instrument. Possible values: ,                                                                                                                                                               |
| underlying_symbol | string  | The symbol of the underlying asset.                                                                                                                                                                                 |
| instrument_key    | string  | The unique identifier used across Upstox APIs for instrument identification. For the regex pattern applicable to this field, see the [Field Pattern Appendix](/developer/api-documentation/appendix/field-pattern). |
| strike_price      | number  | The strike price for the option.                                                                                                                                                                                    |
| lot_size          | number  | The size of one lot of the option.                                                                                                                                                                                  |
| freeze_quantity   | number  | The maximum quantity that can be frozen.                                                                                                                                                                            |
| exchange_token    | string  | The exchange-specific token for the option.                                                                                                                                                                         |
| minimum_lot       | number  | The minimum lot size for the option.                                                                                                                                                                                |
| underlying_key    | string  | The for the underlying asset.                                                                                                                                                                                       |
| tick_size         | number  | The minimum price movement of the option.                                                                                                                                                                           |
| underlying_type   | string  | The type of the underlying asset. Possible values: , , , ,                                                                                                                                                          |
| trading_symbol    | string  | The symbol used for trading the option. Format:                                                                                                                                                                     |

Note

- When you're searching for instrument keys within an instrument JSON file, you can employ the and parameters to refine and narrow down the list of instrument keys. For instance, if you're looking for the instrument key for NSE Index, specify the as and the as , excluding other segments and instrument types from your search criteria.

### Field Description​

| Field Name | Type   | Description                                    |
| ---------- | ------ | ---------------------------------------------- |
| segment    | string | Segment to which the instrument is associated. |

Possible values: , , , , , , , ,  
name| string| The name of the index.  
exchange| string| Exchange to which the instrument is associated.  
Possible values: , ,  
instrument_type| string| The type of the option instrument.  
Possible values:  
instrument_key| string| The unique identifier used across Upstox APIs for instrument identification. For the regex pattern applicable to this field, see the [Field Pattern Appendix](/developer/api-documentation/appendix/field-pattern).  
exchange_token| number| The numerical identifier issued by the exchange representing the instrument.  
trading_symbol| string| Trading symbol for the index.

Note

- The files undergo daily refresh at around 6 AM, and they are only refreshed as needed during the day, which is a seldom occurrence.
- The BOD instrument for the next trading day will not include delisted stocks or expired contracts.

[PreviousSelf Generated](/developer/api-documentation/self-generated-sdk)[NextLogin](/developer/api-documentation/login)

- CSV Files
  - Sample CSV Record
  - Field Description
- JSON files
  - Sample JSON Object
  - Field Description

---

## [Instruments | Upstox Developer API](https://upstox.com/developer/api-documentation/instruments#json-files)

- [](/developer/api-documentation/)
- [Developer API](/developer/api-documentation/open-api)
- Instruments

On this page

# Instruments

Note

- **The CSV format for instruments files is being deprecated.** Switch to the JSON format for improved performance. Details at [CSV Instruments File Deprecation Notice](/developer/api-documentation/announcements/instruments-csv-deprecation-notice).
- The list of suspended instruments is available in the [JSON section](/developer/api-documentation/instruments#json-files) below.

Recommendations

- Use for uniquely identifying instruments, as it remains unique for each instrument. Conversely, may be reused by the exchange for a different instrument after its expiry.
- Use Instruments data in JSON format instead of CSV, as its structure has been designed for enhanced robustness and future scalability, making programmatic processing easier.

## CSV Files​

These URLs provide access to the complete list of BOD contracts available for trading on Upstox in CSV format.

- [Complete](https://assets.upstox.com/market-quote/instruments/exchange/complete.csv.gz)
- [NSE](https://assets.upstox.com/market-quote/instruments/exchange/NSE.csv.gz)
- [BSE](https://assets.upstox.com/market-quote/instruments/exchange/BSE.csv.gz)
- [MCX](https://assets.upstox.com/market-quote/instruments/exchange/MCX.csv.gz)

### Sample CSV Record​

| instrument_key | exchange_token | tradingsymbol | name                | last_price              | expiry | strike     | tick_size | lot_size | instrument_type | option_type | exchange |
| -------------- | -------------- | ------------- | ------------------- | ----------------------- | ------ | ---------- | --------- | -------- | --------------- | ----------- | -------- | ------ |
| NSE_FO         | 164693         | 164693        | RELIANCE24JAN1840CE | RELIANCE INDUSTRIES LTD | 424.8  | 2024-01-25 | 1840.0    | 0.05     | 250             | OPTSTK      | CE       | NSE_FO |

### Field Description​

| Name            | Type   | Description                                                                                                                                                                                                                                                          |
| --------------- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| instrument_key  | string | The unique identifier used across Upstox APIs for instrument identification. For the regex pattern applicable to this field, see the [Field Pattern Appendix](/developer/api-documentation/appendix/field-pattern).                                                  |
| exchange_token  | number | The numerical identifier issued by the exchange representing the instrument.                                                                                                                                                                                         |
| tradingsymbol   | string | Shows the trading symbol which could be a combination of symbol name, instrument, expiry date etc. The format of this value may vary between weekly and monthly contracts, leading to inconsistencies. These inconsistencies have been resolved in the JSON version. |
| name            | string | Name of the company (for equity instruments).                                                                                                                                                                                                                        |
| last_price      | number | Last traded price.                                                                                                                                                                                                                                                   |
| expiry          | string | Expiry date (for derivatives). Data format is                                                                                                                                                                                                                        |
| strike          | number | Indicates the predetermined price at which an option can be bought or sold when it's exercised.                                                                                                                                                                      |
| tick_size       | number | Measure of the minimum upward or downward movement in the price of an instrument.                                                                                                                                                                                    |
| lot_size        | number | Minimum size in which the stock futures or index futures can be traded.                                                                                                                                                                                              |
| instrument_type | string | Instrument type of a particular contract.                                                                                                                                                                                                                            |

Possible values: , , etc.  
option_type| string| Option type of the option contracts (applicable only for options contract).  
Possible values: ,  
exchange| string| Exchange to which the order is associated.  
Possible values: , , , , , etc.

## JSON files​

These URLs provide access to the complete list of BOD contracts available for trading on Upstox in JSON format.

- [Complete](https://assets.upstox.com/market-quote/instruments/exchange/complete.json.gz)
- [NSE](https://assets.upstox.com/market-quote/instruments/exchange/NSE.json.gz)
- [BSE](https://assets.upstox.com/market-quote/instruments/exchange/BSE.json.gz)
- [MCX](https://assets.upstox.com/market-quote/instruments/exchange/MCX.json.gz)
- [Suspended](https://assets.upstox.com/market-quote/instruments/exchange/suspended-instrument.json.gz)

### Sample JSON Object​

- EQ
- Futures
- Options
- INDEX

Note

- When you're searching for instrument keys within an instrument JSON file, you can employ the and parameters to refine and narrow down the list of instrument keys. For instance, if you're looking for the instrument key for Reliance Equity, specify the as and the as , excluding other segments and instrument types from your search criteria.

### Field Description

| Field Name | Type   | Description                                    |
| ---------- | ------ | ---------------------------------------------- |
| segment    | string | Segment to which the instrument is associated. |

Possible values: , , , , , , , ,  
name| string| The name of the equity.  
exchange| string| Exchange to which the instrument is associated.  
Possible values: , ,  
isin| string| The International Securities Identification Number.  
instrument_type| string| The instrument types for NSE are present at [NSE India](https://www.nseindia.com/market-data/legend-of-series) and for BSE are present at [BSE India](https://www.bseindia.com/markets/equity/EQReports/tra_trading.aspx).  
instrument_key| string| The unique identifier used across Upstox APIs for instrument identification. For the regex pattern applicable to this field, see the [Field Pattern Appendix](/developer/api-documentation/appendix/field-pattern).  
lot_size| number| The size of one lot of the equity.  
freeze_quantity| number| The maximum quantity that can be frozen.  
exchange_token| string| The exchange-specific token for the equity.  
tick_size| number| The minimum price movement of the equity.  
trading_symbol| string| Trading symbol of the instrument.  
short_name| string| A shorter or abbreviated name of the equity.  
security_type| string| Identifies the classification or status of a security within the market. Valid security types can be found in the [Security Type Appendix](/developer/api-documentation/appendix/equity-security-type)

Note

- When you're searching for instrument keys within an instrument JSON file, you can employ the and parameters to refine and narrow down the list of instrument keys. For instance, if you're looking for the instrument key for Reliance Future, specify the as and the as , excluding other segments and instrument types from your search criteria.

### Field Description

| Field Name        | Type    | Description                                                                                                                                                                                                         |
| ----------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| weekly            | boolean | Indicates if the future is weekly.                                                                                                                                                                                  |
| segment           | string  | Segment to which the instrument is associated. Possible values: , , , , , , , ,                                                                                                                                     |
| name              | string  | The name of the future.                                                                                                                                                                                             |
| exchange          | string  | Exchange to which the instrument is associated. Possible values: , ,                                                                                                                                                |
| expiry            | date    | The expiry date of the future.                                                                                                                                                                                      |
| instrument_type   | string  | The type of the future instrument. Possible values:                                                                                                                                                                 |
| underlying_symbol | string  | The symbol of the underlying asset.                                                                                                                                                                                 |
| instrument_key    | string  | The unique identifier used across Upstox APIs for instrument identification. For the regex pattern applicable to this field, see the [Field Pattern Appendix](/developer/api-documentation/appendix/field-pattern). |
| lot_size          | number  | The size of one lot of the future.                                                                                                                                                                                  |
| freeze_quantity   | number  | The maximum quantity that can be frozen.                                                                                                                                                                            |
| exchange_token    | string  | The exchange-specific token for the future.                                                                                                                                                                         |
| minimum_lot       | number  | The minimum lot size for the future.                                                                                                                                                                                |
| underlying_key    | string  | The for the underlying asset.                                                                                                                                                                                       |
| tick_size         | number  | The minimum price movement of the future.                                                                                                                                                                           |
| underlying_type   | string  | The type of the underlying asset. Possible values: , , , ,                                                                                                                                                          |
| trading_symbol    | string  | The symbol used for trading the future. Format:                                                                                                                                                                     |

Note

- When you're searching for instrument keys within an instrument JSON file, you can employ the and parameters to refine and narrow down the list of instrument keys. For instance, if you're looking for the instrument key for Reliance Call Option, specify the as and the as , excluding other segments and instrument types from your search criteria. If you want to search for Put Option then set as .

### Field Description

| Field Name        | Type    | Description                                                                                                                                                                                                         |
| ----------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| weekly            | boolean | Indicates if the option is weekly.                                                                                                                                                                                  |
| segment           | string  | The market segment of the option. Possible values: , , , , , , , ,                                                                                                                                                  |
| name              | string  | The name of the option.                                                                                                                                                                                             |
| exchange          | string  | Exchange to which the instrument is associated. Possible values: , ,                                                                                                                                                |
| expiry            | date    | The expiry date of the option.                                                                                                                                                                                      |
| instrument_type   | string  | The type of the option instrument. Possible values: ,                                                                                                                                                               |
| underlying_symbol | string  | The symbol of the underlying asset.                                                                                                                                                                                 |
| instrument_key    | string  | The unique identifier used across Upstox APIs for instrument identification. For the regex pattern applicable to this field, see the [Field Pattern Appendix](/developer/api-documentation/appendix/field-pattern). |
| strike_price      | number  | The strike price for the option.                                                                                                                                                                                    |
| lot_size          | number  | The size of one lot of the option.                                                                                                                                                                                  |
| freeze_quantity   | number  | The maximum quantity that can be frozen.                                                                                                                                                                            |
| exchange_token    | string  | The exchange-specific token for the option.                                                                                                                                                                         |
| minimum_lot       | number  | The minimum lot size for the option.                                                                                                                                                                                |
| underlying_key    | string  | The for the underlying asset.                                                                                                                                                                                       |
| tick_size         | number  | The minimum price movement of the option.                                                                                                                                                                           |
| underlying_type   | string  | The type of the underlying asset. Possible values: , , , ,                                                                                                                                                          |
| trading_symbol    | string  | The symbol used for trading the option. Format:                                                                                                                                                                     |

Note

- When you're searching for instrument keys within an instrument JSON file, you can employ the and parameters to refine and narrow down the list of instrument keys. For instance, if you're looking for the instrument key for NSE Index, specify the as and the as , excluding other segments and instrument types from your search criteria.

### Field Description​

| Field Name | Type   | Description                                    |
| ---------- | ------ | ---------------------------------------------- |
| segment    | string | Segment to which the instrument is associated. |

Possible values: , , , , , , , ,  
name| string| The name of the index.  
exchange| string| Exchange to which the instrument is associated.  
Possible values: , ,  
instrument_type| string| The type of the option instrument.  
Possible values:  
instrument_key| string| The unique identifier used across Upstox APIs for instrument identification. For the regex pattern applicable to this field, see the [Field Pattern Appendix](/developer/api-documentation/appendix/field-pattern).  
exchange_token| number| The numerical identifier issued by the exchange representing the instrument.  
trading_symbol| string| Trading symbol for the index.

Note

- The files undergo daily refresh at around 6 AM, and they are only refreshed as needed during the day, which is a seldom occurrence.
- The BOD instrument for the next trading day will not include delisted stocks or expired contracts.

[PreviousSelf Generated](/developer/api-documentation/self-generated-sdk)[NextLogin](/developer/api-documentation/login)

- CSV Files
  - Sample CSV Record
  - Field Description
- JSON files
  - Sample JSON Object
  - Field Description

---

## [CSV Instruments File Deprecation Notice | Upstox Developer API](https://upstox.com/developer/api-documentation/announcements/instruments-csv-deprecation-notice)

On this page

## CSV Instruments File Deprecation Notice​

**Effective Immediately**

We are announcing the upcoming deprecation of the CSV format for our instruments file. This move is aimed at enhancing performance and scalability through the JSON format.

### What's Changing?​

- **Deprecation of CSV Format:** The CSV version of the instruments file will soon be discontinued. We urge all users to transition to the JSON version to avoid any disruption in service.

### Recommended Actions​

- **Begin Transition to JSON:** Start updating your systems to utilize the JSON format for instruments files. This format offers enhanced performance and scalability, ensuring a smoother and more efficient experience.

- **Deprecation Date Announcement:** The specific date for the CSV format deprecation will be communicated shortly. We are providing this advance notice to allow ample time for planning and transition.

### Support and Queries​

For any questions or additional support regarding this deprecation, please visit our developer community at <https://community.upstox.com/c/developer-api/>. Our team is ready to assist you in making this transition as smooth as possible.

We appreciate your attention to this matter and your ongoing cooperation.

- CSV Instruments File Deprecation Notice
  - What's Changing?
  - Recommended Actions
  - Support and Queries

---

## [New URL and Simplified Headers | Upstox Developer API](https://upstox.com/developer/api-documentation/announcements/new-url-and-simplified-headers)

On this page

## New URL and Simplified Headers​

**Effective Immediately**

We are pleased to announce a significant update to the Upstox API Service. This change is part of our ongoing commitment to enhance usability and service efficiency.

### What's Changing?​

1. **New Base URL:** The base URL for accessing the Upstox API has been updated to . This change is designed to streamline our API structure for more intuitive access.

2. **Simplified Header Requirements:** Alongside the new URL, we have updated our header requirements. The 'Api Version' header, previously mandatory and set to 2.0, will no longer be required for API calls to the new URL. This modification reduces the complexity of constructing API requests.

### Transition Period​

- **Dual Endpoint Availability:** To ensure a seamless transition, both the old URL () and the new URL () will be operational for a transitional period. This approach ensures that your existing integrations continue to work without immediate disruption.

- **Recommended Action:** While your existing setups using the old URL will continue to function during this phase, we encourage you to migrate to the new URL and updated header configuration as soon as convenient for you.

### Migration Steps:​

1. **Update the Base URL:** Change the base URL in your API integrations from to .

2. **Remove the 'Api Version' Header:** Adjust your API requests to eliminate the 'Api Version' header.

We appreciate your cooperation during this transition and thank you for your continued partnership. Our team is committed to continually enhancing our services to better meet your needs.

- New URL and Simplified Headers
  - What's Changing?
  - Transition Period
  - Migration Steps:

---

## [Authentication | Upstox Developer API](https://upstox.com/developer/api-documentation/authentication#docusaurus_skipToContent_fallback)

- [](/developer/api-documentation/)
- [Developer API](/developer/api-documentation/open-api)
- Authentication

On this page

# Authentication

![Login flow](/developer/api-documentation/assets/images/loginflow-58e94762548c9142d35fe1d479df21bf.webp#block)

Upstox uses standard OAuth 2.0 for customer authentication and login.

All logins are handled by upstox.com. There is no public endpoint for other applications to directly log the customer into their upstox.com. For security and compliance purposes, all logins and logouts are handled exclusively by upstox.com.

## Perform Authentication​

The login window is a web page hosted at the following link.

Your client application must trigger the opening of the above URL using Webview (or similar technology) and pass the following parameters:

| Parameter     | Description                                                                                                                             |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| client_id     | The API key obtained during the app generation process.                                                                                 |
| redirect_uri  | The URL to which the user will be redirected post authentication; must match the URL provided during app generation.                    |
| state         | An optional parameter. If specified, will be returned after authentication, allowing for state continuity between request and callback. |
| response_type | This value must always be .                                                                                                             |

URL construction:

Sample URL:

NOTE

In OAuth, client_id means API Key (not customer UCC) and client_secret means API Secret.

NOTE

If you encounter an error, it likely stems from inconsistencies in the request parameters (, , and ) compared to the information registered during app creation. Ensure you verify these parameters and correct any discrepancies before making another attempt.

The user will be redirected to the default login page where they will be able to log in.

![Login page](/developer/api-documentation/assets/images/loginpage-bd1c2065c2c8d2c720f0ed703dd48131.webp#block)

NOTE

You also have the option to select [TOTP (Time-based One-Time Password)](https://en.wikipedia.org/wiki/Time-based_one-time_password) as a more secure method for 2FA, compared to the usual SMS OTP, for a safer login. Learn more about activating TOTP on your Upstox account [here](https://help.upstox.com/support/solutions/articles/260346-what-is-totp-and-how-to-enable-totp-for-my-account-from-upstox-web-platform-).

## Receive Auth Code​

Upon successful authentication, this API will redirect to the URL specified in the parameter, with the essential for the token generation included within the request parameters.

| Name  | Description                                                                     |
| ----- | ------------------------------------------------------------------------------- |
| code  | Utilize this code to generate the as part of the next step.                     |
| state | Provided optionally if it was initially included in the request URL parameters. |

## Generate Access Token​

Once the user has authenticated with us, they will be redirected to your redirect URL with an authorization code. The parameter will come as (query parameter).

NOTE

The authorization code is valid for a single use, regardless of whether the access token generation succeeds or encounters an issue.

The last step is to make a server-to-server call between your backend server and Upstox to get an using the authorization code. This can be done by calling the following service:

You will need to pass the following parameters:

| Parameter     | Description                                                                                                                                                   |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| code          | The is a unique parameter included in the URL upon a successful [Authorize API](/developer/api-documentation/authorize) authentication.                       |
| client_id     | The API key obtained during the app generation process.                                                                                                       |
| client_secret | The API secret obtained during the app generation process. This private key remains confidential, known only to the application and the authorization server. |
| redirect_uri  | The URL provided during app generation.                                                                                                                       |
| grant_type    | This value must always be .                                                                                                                                   |

URL construction:

Finally this will return an access token for you. This access token can be successfully passed back to your front-end application to access the Upstox API.

## Extended Token​

Upstox APIs now support the generation of an extended token in addition to the standard access token.

An extended token is designed for long-term use, primarily for read-only API calls. It remains valid for one year from the date it is generated, or until the user revokes access to their account from pro.upstox.com, whichever occurs first. This token allows access to specific user trade data. Below is a list of APIs that can be utilized with the extended token:

#### Supported APIs​

- [Get Positions](/developer/api-documentation/get-positions)
- [Get Holdings](/developer/api-documentation/get-holdings)
- [Get Order Details](/developer/api-documentation/get-order-details)
- [Get Order History](/developer/api-documentation/get-order-history)
- [Get Order Book](/developer/api-documentation/get-order-book)

Enroll for Extended Token

Extended tokens are available for multi-client applications upon request. If your app requires an extended token, please reach out to our support team for enrollment and further assistance.

[PreviousDeveloper API](/developer/api-documentation/open-api)[NextAPI Structure](/developer/api-documentation/request-response)

- Perform Authentication
- Receive Auth Code
- Generate Access Token
- Extended Token

---

## [Authentication | Upstox Developer API](https://upstox.com/developer/api-documentation/authentication#perform-authentication)

- [](/developer/api-documentation/)
- [Developer API](/developer/api-documentation/open-api)
- Authentication

On this page

# Authentication

![Login flow](/developer/api-documentation/assets/images/loginflow-58e94762548c9142d35fe1d479df21bf.webp#block)

Upstox uses standard OAuth 2.0 for customer authentication and login.

All logins are handled by upstox.com. There is no public endpoint for other applications to directly log the customer into their upstox.com. For security and compliance purposes, all logins and logouts are handled exclusively by upstox.com.

## Perform Authentication​

The login window is a web page hosted at the following link.

Your client application must trigger the opening of the above URL using Webview (or similar technology) and pass the following parameters:

| Parameter     | Description                                                                                                                             |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| client_id     | The API key obtained during the app generation process.                                                                                 |
| redirect_uri  | The URL to which the user will be redirected post authentication; must match the URL provided during app generation.                    |
| state         | An optional parameter. If specified, will be returned after authentication, allowing for state continuity between request and callback. |
| response_type | This value must always be .                                                                                                             |

URL construction:

Sample URL:

NOTE

In OAuth, client_id means API Key (not customer UCC) and client_secret means API Secret.

NOTE

If you encounter an error, it likely stems from inconsistencies in the request parameters (, , and ) compared to the information registered during app creation. Ensure you verify these parameters and correct any discrepancies before making another attempt.

The user will be redirected to the default login page where they will be able to log in.

![Login page](/developer/api-documentation/assets/images/loginpage-bd1c2065c2c8d2c720f0ed703dd48131.webp#block)

NOTE

You also have the option to select [TOTP (Time-based One-Time Password)](https://en.wikipedia.org/wiki/Time-based_one-time_password) as a more secure method for 2FA, compared to the usual SMS OTP, for a safer login. Learn more about activating TOTP on your Upstox account [here](https://help.upstox.com/support/solutions/articles/260346-what-is-totp-and-how-to-enable-totp-for-my-account-from-upstox-web-platform-).

## Receive Auth Code​

Upon successful authentication, this API will redirect to the URL specified in the parameter, with the essential for the token generation included within the request parameters.

| Name  | Description                                                                     |
| ----- | ------------------------------------------------------------------------------- |
| code  | Utilize this code to generate the as part of the next step.                     |
| state | Provided optionally if it was initially included in the request URL parameters. |

## Generate Access Token​

Once the user has authenticated with us, they will be redirected to your redirect URL with an authorization code. The parameter will come as (query parameter).

NOTE

The authorization code is valid for a single use, regardless of whether the access token generation succeeds or encounters an issue.

The last step is to make a server-to-server call between your backend server and Upstox to get an using the authorization code. This can be done by calling the following service:

You will need to pass the following parameters:

| Parameter     | Description                                                                                                                                                   |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| code          | The is a unique parameter included in the URL upon a successful [Authorize API](/developer/api-documentation/authorize) authentication.                       |
| client_id     | The API key obtained during the app generation process.                                                                                                       |
| client_secret | The API secret obtained during the app generation process. This private key remains confidential, known only to the application and the authorization server. |
| redirect_uri  | The URL provided during app generation.                                                                                                                       |
| grant_type    | This value must always be .                                                                                                                                   |

URL construction:

Finally this will return an access token for you. This access token can be successfully passed back to your front-end application to access the Upstox API.

## Extended Token​

Upstox APIs now support the generation of an extended token in addition to the standard access token.

An extended token is designed for long-term use, primarily for read-only API calls. It remains valid for one year from the date it is generated, or until the user revokes access to their account from pro.upstox.com, whichever occurs first. This token allows access to specific user trade data. Below is a list of APIs that can be utilized with the extended token:

#### Supported APIs​

- [Get Positions](/developer/api-documentation/get-positions)
- [Get Holdings](/developer/api-documentation/get-holdings)
- [Get Order Details](/developer/api-documentation/get-order-details)
- [Get Order History](/developer/api-documentation/get-order-history)
- [Get Order Book](/developer/api-documentation/get-order-book)

Enroll for Extended Token

Extended tokens are available for multi-client applications upon request. If your app requires an extended token, please reach out to our support team for enrollment and further assistance.

[PreviousDeveloper API](/developer/api-documentation/open-api)[NextAPI Structure](/developer/api-documentation/request-response)

- Perform Authentication
- Receive Auth Code
- Generate Access Token
- Extended Token

---

## [Authentication | Upstox Developer API](https://upstox.com/developer/api-documentation/authentication#receive-auth-code)

- [](/developer/api-documentation/)
- [Developer API](/developer/api-documentation/open-api)
- Authentication

On this page

# Authentication

![Login flow](/developer/api-documentation/assets/images/loginflow-58e94762548c9142d35fe1d479df21bf.webp#block)

Upstox uses standard OAuth 2.0 for customer authentication and login.

All logins are handled by upstox.com. There is no public endpoint for other applications to directly log the customer into their upstox.com. For security and compliance purposes, all logins and logouts are handled exclusively by upstox.com.

## Perform Authentication​

The login window is a web page hosted at the following link.

Your client application must trigger the opening of the above URL using Webview (or similar technology) and pass the following parameters:

| Parameter     | Description                                                                                                                             |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| client_id     | The API key obtained during the app generation process.                                                                                 |
| redirect_uri  | The URL to which the user will be redirected post authentication; must match the URL provided during app generation.                    |
| state         | An optional parameter. If specified, will be returned after authentication, allowing for state continuity between request and callback. |
| response_type | This value must always be .                                                                                                             |

URL construction:

Sample URL:

NOTE

In OAuth, client_id means API Key (not customer UCC) and client_secret means API Secret.

NOTE

If you encounter an error, it likely stems from inconsistencies in the request parameters (, , and ) compared to the information registered during app creation. Ensure you verify these parameters and correct any discrepancies before making another attempt.

The user will be redirected to the default login page where they will be able to log in.

![Login page](/developer/api-documentation/assets/images/loginpage-bd1c2065c2c8d2c720f0ed703dd48131.webp#block)

NOTE

You also have the option to select [TOTP (Time-based One-Time Password)](https://en.wikipedia.org/wiki/Time-based_one-time_password) as a more secure method for 2FA, compared to the usual SMS OTP, for a safer login. Learn more about activating TOTP on your Upstox account [here](https://help.upstox.com/support/solutions/articles/260346-what-is-totp-and-how-to-enable-totp-for-my-account-from-upstox-web-platform-).

## Receive Auth Code​

Upon successful authentication, this API will redirect to the URL specified in the parameter, with the essential for the token generation included within the request parameters.

| Name  | Description                                                                     |
| ----- | ------------------------------------------------------------------------------- |
| code  | Utilize this code to generate the as part of the next step.                     |
| state | Provided optionally if it was initially included in the request URL parameters. |

## Generate Access Token​

Once the user has authenticated with us, they will be redirected to your redirect URL with an authorization code. The parameter will come as (query parameter).

NOTE

The authorization code is valid for a single use, regardless of whether the access token generation succeeds or encounters an issue.

The last step is to make a server-to-server call between your backend server and Upstox to get an using the authorization code. This can be done by calling the following service:

You will need to pass the following parameters:

| Parameter     | Description                                                                                                                                                   |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| code          | The is a unique parameter included in the URL upon a successful [Authorize API](/developer/api-documentation/authorize) authentication.                       |
| client_id     | The API key obtained during the app generation process.                                                                                                       |
| client_secret | The API secret obtained during the app generation process. This private key remains confidential, known only to the application and the authorization server. |
| redirect_uri  | The URL provided during app generation.                                                                                                                       |
| grant_type    | This value must always be .                                                                                                                                   |

URL construction:

Finally this will return an access token for you. This access token can be successfully passed back to your front-end application to access the Upstox API.

## Extended Token​

Upstox APIs now support the generation of an extended token in addition to the standard access token.

An extended token is designed for long-term use, primarily for read-only API calls. It remains valid for one year from the date it is generated, or until the user revokes access to their account from pro.upstox.com, whichever occurs first. This token allows access to specific user trade data. Below is a list of APIs that can be utilized with the extended token:

#### Supported APIs​

- [Get Positions](/developer/api-documentation/get-positions)
- [Get Holdings](/developer/api-documentation/get-holdings)
- [Get Order Details](/developer/api-documentation/get-order-details)
- [Get Order History](/developer/api-documentation/get-order-history)
- [Get Order Book](/developer/api-documentation/get-order-book)

Enroll for Extended Token

Extended tokens are available for multi-client applications upon request. If your app requires an extended token, please reach out to our support team for enrollment and further assistance.

[PreviousDeveloper API](/developer/api-documentation/open-api)[NextAPI Structure](/developer/api-documentation/request-response)

- Perform Authentication
- Receive Auth Code
- Generate Access Token
- Extended Token

---

## [Authentication | Upstox Developer API](https://upstox.com/developer/api-documentation/authentication#generate-access-token)

- [](/developer/api-documentation/)
- [Developer API](/developer/api-documentation/open-api)
- Authentication

On this page

# Authentication

![Login flow](/developer/api-documentation/assets/images/loginflow-58e94762548c9142d35fe1d479df21bf.webp#block)

Upstox uses standard OAuth 2.0 for customer authentication and login.

All logins are handled by upstox.com. There is no public endpoint for other applications to directly log the customer into their upstox.com. For security and compliance purposes, all logins and logouts are handled exclusively by upstox.com.

## Perform Authentication​

The login window is a web page hosted at the following link.

Your client application must trigger the opening of the above URL using Webview (or similar technology) and pass the following parameters:

| Parameter     | Description                                                                                                                             |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| client_id     | The API key obtained during the app generation process.                                                                                 |
| redirect_uri  | The URL to which the user will be redirected post authentication; must match the URL provided during app generation.                    |
| state         | An optional parameter. If specified, will be returned after authentication, allowing for state continuity between request and callback. |
| response_type | This value must always be .                                                                                                             |

URL construction:

Sample URL:

NOTE

In OAuth, client_id means API Key (not customer UCC) and client_secret means API Secret.

NOTE

If you encounter an error, it likely stems from inconsistencies in the request parameters (, , and ) compared to the information registered during app creation. Ensure you verify these parameters and correct any discrepancies before making another attempt.

The user will be redirected to the default login page where they will be able to log in.

![Login page](/developer/api-documentation/assets/images/loginpage-bd1c2065c2c8d2c720f0ed703dd48131.webp#block)

NOTE

You also have the option to select [TOTP (Time-based One-Time Password)](https://en.wikipedia.org/wiki/Time-based_one-time_password) as a more secure method for 2FA, compared to the usual SMS OTP, for a safer login. Learn more about activating TOTP on your Upstox account [here](https://help.upstox.com/support/solutions/articles/260346-what-is-totp-and-how-to-enable-totp-for-my-account-from-upstox-web-platform-).

## Receive Auth Code​

Upon successful authentication, this API will redirect to the URL specified in the parameter, with the essential for the token generation included within the request parameters.

| Name  | Description                                                                     |
| ----- | ------------------------------------------------------------------------------- |
| code  | Utilize this code to generate the as part of the next step.                     |
| state | Provided optionally if it was initially included in the request URL parameters. |

## Generate Access Token​

Once the user has authenticated with us, they will be redirected to your redirect URL with an authorization code. The parameter will come as (query parameter).

NOTE

The authorization code is valid for a single use, regardless of whether the access token generation succeeds or encounters an issue.

The last step is to make a server-to-server call between your backend server and Upstox to get an using the authorization code. This can be done by calling the following service:

You will need to pass the following parameters:

| Parameter     | Description                                                                                                                                                   |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| code          | The is a unique parameter included in the URL upon a successful [Authorize API](/developer/api-documentation/authorize) authentication.                       |
| client_id     | The API key obtained during the app generation process.                                                                                                       |
| client_secret | The API secret obtained during the app generation process. This private key remains confidential, known only to the application and the authorization server. |
| redirect_uri  | The URL provided during app generation.                                                                                                                       |
| grant_type    | This value must always be .                                                                                                                                   |

URL construction:

Finally this will return an access token for you. This access token can be successfully passed back to your front-end application to access the Upstox API.

## Extended Token​

Upstox APIs now support the generation of an extended token in addition to the standard access token.

An extended token is designed for long-term use, primarily for read-only API calls. It remains valid for one year from the date it is generated, or until the user revokes access to their account from pro.upstox.com, whichever occurs first. This token allows access to specific user trade data. Below is a list of APIs that can be utilized with the extended token:

#### Supported APIs​

- [Get Positions](/developer/api-documentation/get-positions)
- [Get Holdings](/developer/api-documentation/get-holdings)
- [Get Order Details](/developer/api-documentation/get-order-details)
- [Get Order History](/developer/api-documentation/get-order-history)
- [Get Order Book](/developer/api-documentation/get-order-book)

Enroll for Extended Token

Extended tokens are available for multi-client applications upon request. If your app requires an extended token, please reach out to our support team for enrollment and further assistance.

[PreviousDeveloper API](/developer/api-documentation/open-api)[NextAPI Structure](/developer/api-documentation/request-response)

- Perform Authentication
- Receive Auth Code
- Generate Access Token
- Extended Token

---

## [Authorize | Upstox Developer API](https://upstox.com/developer/api-documentation/authorize)

- [](/developer/api-documentation/)
- [Developer API](/developer/api-documentation/open-api)
- [Login](/developer/api-documentation/login)
- Authorize

## Authorize​

The authorization flow initiates a redirection to the Upstox login page, with necessary information. Upon a successful user login, the user is then redirected to the specified "redirect_uri" with an authorization code. This code should be utilized in the subsequent step to acquire the access token in the [get token](/developer/api-documentation/get-token) API.

NOTE

- While creating app provide a which is in your control rather than a public endpoint.
- Additionally, it's important to generate a random value for the state parameter and subsequently validate whether the value returned matches the one you originally sent. This helps ensure the security and integrity of your application.
- The QR code login is not compatible with the login flow of the Upstox API.

### Query Parameters​

| Name          | Required | Type   | Description                                                                                                                             |
| ------------- | -------- | ------ | --------------------------------------------------------------------------------------------------------------------------------------- |
| client_id     | true     | string | The API key obtained during the app generation process.                                                                                 |
| redirect_uri  | true     | string | The URL to which the user will be redirected post authentication; must match the URL provided during app generation.                    |
| state         | false    | string | An optional parameter. If specified, will be returned after authentication, allowing for state continuity between request and callback. |
| response_type | true     | string | This value must always be .                                                                                                             |

**Responses**

- 302
- 4XX

---

Upon successful authentication, this API will redirect to the URL specified in the parameter, with the essential for the token generation included within the request parameters.

| Name  | Description                                                                                            |
| ----- | ------------------------------------------------------------------------------------------------------ |
| code  | Utilize this code to generate the through the [Get Token API](/developer/api-documentation/get-token). |
| state | Provided optionally if it was initially included in the request URL parameters.                        |

| Error code  | Description                                                                                                                                           |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| UDAPI100068 | **Check your 'client_id' and 'redirect_uri'; one or both are incorrect.** \- Thrown when one of the credentials you've passed to this API is invalid. |

Loading...

[PreviousLogin](/developer/api-documentation/login)[NextGet Token](/developer/api-documentation/get-token)

---

## [Authentication | Upstox Developer API](https://upstox.com/developer/api-documentation/authentication#extended-token)

- [](/developer/api-documentation/)
- [Developer API](/developer/api-documentation/open-api)
- Authentication

On this page

# Authentication

![Login flow](/developer/api-documentation/assets/images/loginflow-58e94762548c9142d35fe1d479df21bf.webp#block)

Upstox uses standard OAuth 2.0 for customer authentication and login.

All logins are handled by upstox.com. There is no public endpoint for other applications to directly log the customer into their upstox.com. For security and compliance purposes, all logins and logouts are handled exclusively by upstox.com.

## Perform Authentication​

The login window is a web page hosted at the following link.

Your client application must trigger the opening of the above URL using Webview (or similar technology) and pass the following parameters:

| Parameter     | Description                                                                                                                             |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| client_id     | The API key obtained during the app generation process.                                                                                 |
| redirect_uri  | The URL to which the user will be redirected post authentication; must match the URL provided during app generation.                    |
| state         | An optional parameter. If specified, will be returned after authentication, allowing for state continuity between request and callback. |
| response_type | This value must always be .                                                                                                             |

URL construction:

Sample URL:

NOTE

In OAuth, client_id means API Key (not customer UCC) and client_secret means API Secret.

NOTE

If you encounter an error, it likely stems from inconsistencies in the request parameters (, , and ) compared to the information registered during app creation. Ensure you verify these parameters and correct any discrepancies before making another attempt.

The user will be redirected to the default login page where they will be able to log in.

![Login page](/developer/api-documentation/assets/images/loginpage-bd1c2065c2c8d2c720f0ed703dd48131.webp#block)

NOTE

You also have the option to select [TOTP (Time-based One-Time Password)](https://en.wikipedia.org/wiki/Time-based_one-time_password) as a more secure method for 2FA, compared to the usual SMS OTP, for a safer login. Learn more about activating TOTP on your Upstox account [here](https://help.upstox.com/support/solutions/articles/260346-what-is-totp-and-how-to-enable-totp-for-my-account-from-upstox-web-platform-).

## Receive Auth Code​

Upon successful authentication, this API will redirect to the URL specified in the parameter, with the essential for the token generation included within the request parameters.

| Name  | Description                                                                     |
| ----- | ------------------------------------------------------------------------------- |
| code  | Utilize this code to generate the as part of the next step.                     |
| state | Provided optionally if it was initially included in the request URL parameters. |

## Generate Access Token​

Once the user has authenticated with us, they will be redirected to your redirect URL with an authorization code. The parameter will come as (query parameter).

NOTE

The authorization code is valid for a single use, regardless of whether the access token generation succeeds or encounters an issue.

The last step is to make a server-to-server call between your backend server and Upstox to get an using the authorization code. This can be done by calling the following service:

You will need to pass the following parameters:

| Parameter     | Description                                                                                                                                                   |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| code          | The is a unique parameter included in the URL upon a successful [Authorize API](/developer/api-documentation/authorize) authentication.                       |
| client_id     | The API key obtained during the app generation process.                                                                                                       |
| client_secret | The API secret obtained during the app generation process. This private key remains confidential, known only to the application and the authorization server. |
| redirect_uri  | The URL provided during app generation.                                                                                                                       |
| grant_type    | This value must always be .                                                                                                                                   |

URL construction:

Finally this will return an access token for you. This access token can be successfully passed back to your front-end application to access the Upstox API.

## Extended Token​

Upstox APIs now support the generation of an extended token in addition to the standard access token.

An extended token is designed for long-term use, primarily for read-only API calls. It remains valid for one year from the date it is generated, or until the user revokes access to their account from pro.upstox.com, whichever occurs first. This token allows access to specific user trade data. Below is a list of APIs that can be utilized with the extended token:

#### Supported APIs​

- [Get Positions](/developer/api-documentation/get-positions)
- [Get Holdings](/developer/api-documentation/get-holdings)
- [Get Order Details](/developer/api-documentation/get-order-details)
- [Get Order History](/developer/api-documentation/get-order-history)
- [Get Order Book](/developer/api-documentation/get-order-book)

Enroll for Extended Token

Extended tokens are available for multi-client applications upon request. If your app requires an extended token, please reach out to our support team for enrollment and further assistance.

[PreviousDeveloper API](/developer/api-documentation/open-api)[NextAPI Structure](/developer/api-documentation/request-response)

- Perform Authentication
- Receive Auth Code
- Generate Access Token
- Extended Token

---

## [Authentication | Upstox Developer API](https://upstox.com/developer/api-documentation/authentication#supported-apis)

- [](/developer/api-documentation/)
- [Developer API](/developer/api-documentation/open-api)
- Authentication

On this page

# Authentication

![Login flow](/developer/api-documentation/assets/images/loginflow-58e94762548c9142d35fe1d479df21bf.webp#block)

Upstox uses standard OAuth 2.0 for customer authentication and login.

All logins are handled by upstox.com. There is no public endpoint for other applications to directly log the customer into their upstox.com. For security and compliance purposes, all logins and logouts are handled exclusively by upstox.com.

## Perform Authentication​

The login window is a web page hosted at the following link.

Your client application must trigger the opening of the above URL using Webview (or similar technology) and pass the following parameters:

| Parameter     | Description                                                                                                                             |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| client_id     | The API key obtained during the app generation process.                                                                                 |
| redirect_uri  | The URL to which the user will be redirected post authentication; must match the URL provided during app generation.                    |
| state         | An optional parameter. If specified, will be returned after authentication, allowing for state continuity between request and callback. |
| response_type | This value must always be .                                                                                                             |

URL construction:

Sample URL:

NOTE

In OAuth, client_id means API Key (not customer UCC) and client_secret means API Secret.

NOTE

If you encounter an error, it likely stems from inconsistencies in the request parameters (, , and ) compared to the information registered during app creation. Ensure you verify these parameters and correct any discrepancies before making another attempt.

The user will be redirected to the default login page where they will be able to log in.

![Login page](/developer/api-documentation/assets/images/loginpage-bd1c2065c2c8d2c720f0ed703dd48131.webp#block)

NOTE

You also have the option to select [TOTP (Time-based One-Time Password)](https://en.wikipedia.org/wiki/Time-based_one-time_password) as a more secure method for 2FA, compared to the usual SMS OTP, for a safer login. Learn more about activating TOTP on your Upstox account [here](https://help.upstox.com/support/solutions/articles/260346-what-is-totp-and-how-to-enable-totp-for-my-account-from-upstox-web-platform-).

## Receive Auth Code​

Upon successful authentication, this API will redirect to the URL specified in the parameter, with the essential for the token generation included within the request parameters.

| Name  | Description                                                                     |
| ----- | ------------------------------------------------------------------------------- |
| code  | Utilize this code to generate the as part of the next step.                     |
| state | Provided optionally if it was initially included in the request URL parameters. |

## Generate Access Token​

Once the user has authenticated with us, they will be redirected to your redirect URL with an authorization code. The parameter will come as (query parameter).

NOTE

The authorization code is valid for a single use, regardless of whether the access token generation succeeds or encounters an issue.

The last step is to make a server-to-server call between your backend server and Upstox to get an using the authorization code. This can be done by calling the following service:

You will need to pass the following parameters:

| Parameter     | Description                                                                                                                                                   |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| code          | The is a unique parameter included in the URL upon a successful [Authorize API](/developer/api-documentation/authorize) authentication.                       |
| client_id     | The API key obtained during the app generation process.                                                                                                       |
| client_secret | The API secret obtained during the app generation process. This private key remains confidential, known only to the application and the authorization server. |
| redirect_uri  | The URL provided during app generation.                                                                                                                       |
| grant_type    | This value must always be .                                                                                                                                   |

URL construction:

Finally this will return an access token for you. This access token can be successfully passed back to your front-end application to access the Upstox API.

## Extended Token​

Upstox APIs now support the generation of an extended token in addition to the standard access token.

An extended token is designed for long-term use, primarily for read-only API calls. It remains valid for one year from the date it is generated, or until the user revokes access to their account from pro.upstox.com, whichever occurs first. This token allows access to specific user trade data. Below is a list of APIs that can be utilized with the extended token:

#### Supported APIs​

- [Get Positions](/developer/api-documentation/get-positions)
- [Get Holdings](/developer/api-documentation/get-holdings)
- [Get Order Details](/developer/api-documentation/get-order-details)
- [Get Order History](/developer/api-documentation/get-order-history)
- [Get Order Book](/developer/api-documentation/get-order-book)

Enroll for Extended Token

Extended tokens are available for multi-client applications upon request. If your app requires an extended token, please reach out to our support team for enrollment and further assistance.

[PreviousDeveloper API](/developer/api-documentation/open-api)[NextAPI Structure](/developer/api-documentation/request-response)

- Perform Authentication
- Receive Auth Code
- Generate Access Token
- Extended Token

---

## [Get Positions | Upstox Developer API](https://upstox.com/developer/api-documentation/get-positions)

- [](/developer/api-documentation/)
- [Developer API](/developer/api-documentation/open-api)
- [Portfolio](/developer/api-documentation/portfolio)
- Get Positions

## Get Positions​

API to retrieve the current positions for the user. These assets remain within the positions portfolio until they are either sold or reach their standard three-month expiration date in the case of derivatives. If any equity positions are carried overnight, they are automatically shifted to the holdings portfolio on the following trading day.

### Header Parameters​

| Name          | Required | Type   | Description                                                                                         |
| ------------- | -------- | ------ | --------------------------------------------------------------------------------------------------- |
| Authorization | true     | string | Requires the format where is obtained from the [Token API](/developer/api-documentation/get-token). |
| Accept        | true     | string | Defines the content format the client expects, which should be set to .                             |

**Responses**

- 200

---

### Response Body​

| Name              | Type     | Description                                                                                                                                        |
| ----------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| status            | string   | A string indicating the outcome of the request. Typically for successful operations.                                                               |
| data              | object[] | Response data for position details                                                                                                                 |
| data[].exchange   | string   | Exchange to which the order is associated. Valid exchanges can be found in the [Exchange Appendix](/developer/api-documentation/appendix/exchange) |
| data[].multiplier | float    | The quantity/lot size multiplier used for calculating P&Ls                                                                                         |
| data[].value      | float    | Net value of the position                                                                                                                          |
| data[].pnl        | float    | Profit and loss - net returns on the position                                                                                                      |
| data[].product    | string   | Signifies if the order was either Intraday, Delivery or CO.                                                                                        |

Possible values: , , , .  
data[].instrument_token| string| Key of the instrument. For the regex pattern applicable to this field, see the [Field Pattern Appendix](/developer/api-documentation/appendix/field-pattern).  
data[].average_price| float| Average price at which the net position quantity was acquired  
data[].buy_value| float| Net value of the bought quantities  
data[].overnight_quantity| int32| Quantity held previously and carried forward over night  
data[].day_buy_value| float| Amount at which the quantity is bought during the day  
data[].day_buy_price| float| Average price at which the day qty was bought. Default is empty string  
data[].overnight_buy_amount| float| Amount at which the quantity was bought in the previous session  
data[].overnight_buy_quantity| int32| Quantity bought in the previous session  
data[].day_buy_quantity| int32| Quantity bought during the day  
data[].day_sell_value| float| Amount at which the quantity is sold during the day  
data[].day_sell_price| float| Average price at which the day quantity was sold  
data[].overnight_sell_amount| float| Amount at which the quantity was sold in the previous session  
data[].overnight_sell_quantity| int32| Quantity sold short in the previous session  
data[].day_sell_quantity| int32| Quantity sold during the day  
data[].quantity| int32| Quantity left after nullifying Day and CF buy quantity towards Day and CF sell quantity  
data[].last_price| float| Last traded market price of the instrument  
data[].unrealised| float| Day PnL generated against open positions  
data[].realised| float| Day PnL generated against closed positions  
data[].sell_value| float| Net value of the sold quantities  
data[].trading_symbol| string| Shows the trading symbol of the instrument  
data[].close_price| float| Closing price of the instrument from the last trading day  
data[].buy_price| float| Average price at which quantities were bought  
data[].sell_price| float| Average price at which quantities were sold

Notice of Deprecation

The lowercase field () is deprecated and will be removed in future versions. Use the snake_case versions for consistency.

## Examples​

A comprehensive set of examples is provided to illustrate various use cases and implementation scenarios for this API. To view detailed examples and access sample code, please refer to: [API Examples](/developer/api-documentation/example-code/portfolio/get-positions).

Loading...

[PreviousPortfolio](/developer/api-documentation/portfolio)[NextConvert Positions](/developer/api-documentation/convert-positions)

---

## [Get Holdings | Upstox Developer API](https://upstox.com/developer/api-documentation/get-holdings)

- [](/developer/api-documentation/)
- [Developer API](/developer/api-documentation/open-api)
- [Portfolio](/developer/api-documentation/portfolio)
- Get Holdings

## Get Holdings​

API to retrieve the long term holdings of the user. A Holding within a holdings portfolio remains in place without a predetermined time limit. It can only be withdrawn when it is divested, delisted, or subject to modifications dictated by the stock exchanges. In essence, the instruments housed in the portfolio are securely located within the user's DEMAT account, in strict compliance with the regulations.

### Header Parameters​

| Name          | Required | Type   | Description                                                                                         |
| ------------- | -------- | ------ | --------------------------------------------------------------------------------------------------- |
| Authorization | true     | string | Requires the format where is obtained from the [Token API](/developer/api-documentation/get-token). |
| Accept        | true     | string | Defines the content format the client expects, which should be set to .                             |

**Responses**

- 200

---

### Response Body​

| Name                     | Type     | Description                                                                          |
| ------------------------ | -------- | ------------------------------------------------------------------------------------ |
| status                   | string   | A string indicating the outcome of the request. Typically for successful operations. |
| data                     | object[] | Response data for holdings                                                           |
| data[].isin              | string   | The standard ISIN representing stocks listed on multiple exchanges                   |
| data[].cnc_used_quantity | int32    | Quantity either blocked towards open or completed order                              |
| data[].collateral_type   | string   | Category of collateral assigned by RMS                                               |
| data[].company_name      | string   | Name of the company                                                                  |
| data[].haircut           | float    | This is the haircut percentage applied from RMS (applicable incase of collateral)    |
| data[].product           | string   | Signifies if the order was either Intraday, Delivery or CO.                          |

Possible values: , , , .  
data[].quantity| int32| The total holding qty  
data[].trading_symbol| string| Shows the trading symbol of the instrument  
data[].last_price| float| The last traded price of the instrument  
data[].close_price| float| Closing price of the instrument from the last trading day  
data[].pnl| float| Profit and Loss  
data[].day_change| float| Day's change in absolute value for the stock  
data[].day_change_percentage| float| Day's change in percentage for the stock  
data[].instrument_token| string| Key of the instrument. For the regex pattern applicable to this field, see the [Field Pattern Appendix](/developer/api-documentation/appendix/field-pattern).  
data[].average_price| float| Average price at which the net holding quantity was acquired  
data[].collateral_quantity| int32| Quantity marked as collateral by RMS on users request  
data[].collateral_update_quantity| int32| Updated collateral quantity  
data[].t1_quantity| int32| Quantity on T+1 day after order execution  
data[].exchange| string| Exchange to which the order is associated. Valid exchanges can be found in the [Exchange Appendix](/developer/api-documentation/appendix/exchange)

Notice of Deprecation

The lowercase field () is deprecated and will be removed in future versions. Use the snake_case versions for consistency.

## Examples​

A comprehensive set of examples is provided to illustrate various use cases and implementation scenarios for this API. To view detailed examples and access sample code, please refer to: [API Examples](/developer/api-documentation/example-code/portfolio/get-holdings).

Loading...

[PreviousConvert Positions](/developer/api-documentation/convert-positions)[NextTrade Profit And Loss](/developer/api-documentation/trade-profit-and-loss)

---

## [Get Order Status | Upstox Developer API](https://upstox.com/developer/api-documentation/get-order-details)

- [](/developer/api-documentation/)
- [Developer API](/developer/api-documentation/open-api)
- [Orders](/developer/api-documentation/orders)
- Get Order Details

## Get Order Details​

API to retrieve the latest status of a specific order. Orders placed by the user remain available for one trading day and are automatically removed at the end of the trading session.

### Header Parameters​

| Name          | Required | Type   | Description                                                                                         |
| ------------- | -------- | ------ | --------------------------------------------------------------------------------------------------- |
| Authorization | true     | string | Requires the format where is obtained from the [Token API](/developer/api-documentation/get-token). |
| Accept        | true     | string | Defines the content format the client expects, which should be set to .                             |

### Query Parameters​

| Name     | Required | Type   | Description                                                                                                                                                                                           |
| -------- | -------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| order_id | false    | string | The order reference ID for which the order status is required. For the regex pattern applicable to this field, see the [Field Pattern Appendix](/developer/api-documentation/appendix/field-pattern). |

**Responses**

- 200
- 4XX

---

### Response Body​

| Name                     | Type    | Description                                                                                                                                                           |
| ------------------------ | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| status                   | string  | A string indicating the outcome of the request. Typically for successful operations.                                                                                  |
| data                     | object  | Response data for order Book                                                                                                                                          |
| data.exchange            | string  | Exchange to which the order is associated. Valid exchanges can be found in the [Exchange Appendix](/developer/api-documentation/appendix/exchange)                    |
| data.product             | string  | Signifies if the order was either Intraday, Delivery or CO.                                                                                                           |
| Possible values: , , , . |
| data.price               | float   | Price at which the order was placed                                                                                                                                   |
| data.quantity            | int32   | Quantity with which the order was placed                                                                                                                              |
| data.status              | string  | Indicates the current status of the order. Valid order statuses can be found in the [Order Status Appendix](/developer/api-documentation/appendix/order-status)       |
| data.tag                 | string  | Tag to uniquely identify an order                                                                                                                                     |
| data.instrument_token    | string  | Key of the instrument. For the regex pattern applicable to this field, see the [Field Pattern Appendix](/developer/api-documentation/appendix/field-pattern).         |
| data.placed_by           | string  | Uniquely identifies the user (commonly referred as UCC)                                                                                                               |
| data.trading_symbol      | string  | Shows the trading symbol of the instrument                                                                                                                            |
| data.order_type          | string  | Type of order. It can be one of the following MARKET refers to market order LIMIT refers to Limit Order SL refers to Stop Loss Limit SL-M refers to Stop Loss Market. |
| Possible values: , , , . |
| data.validity            | string  | It can be one of the following - DAY(default), IOC.                                                                                                                   |
| Possible values: , .     |
| data.trigger_price       | float   | If the order was a stop loss order then the trigger price set is mentioned here                                                                                       |
| data.disclosed_quantity  | int32   | The quantity that should be disclosed in the market depth                                                                                                             |
| data.transaction_type    | string  | Indicates whether its a buy or sell order.                                                                                                                            |
| Possible values: , .     |
| data.average_price       | float   | Average price at which the qty got traded                                                                                                                             |
| data.filled_quantity     | int32   | The total quantity traded from this particular order                                                                                                                  |
| data.pending_quantity    | int32   | Pending quantity to be filled                                                                                                                                         |
| data.status_message      | string  | Indicates the reason when any order is rejected, not modified or cancelled                                                                                            |
| data.status_message_raw  | string  | Description of the order's status as received from RMS                                                                                                                |
| data.exchange_order_id   | string  | Unique order ID assigned by the exchange for the order placed                                                                                                         |
| data.parent_order_id     | string  | In case the order is part of the second of a CO, the parent order ID is indicated here                                                                                |
| data.order_id            | string  | Unique order ID assigned internally for the order placed                                                                                                              |
| data.variety             | string  | Order complexity                                                                                                                                                      |
| data.order_timestamp     | string  | User readable timestamp at which the order was placed                                                                                                                 |
| data.exchange_timestamp  | string  | User readable time at which the order was placed or updated                                                                                                           |
| data.is_amo              | boolean | Signifies if the order is an After Market Order                                                                                                                       |
| data.order_request_id    | string  | Apart from 1st order it shows the count of how many requests were sent                                                                                                |
| data.order_ref_id        | string  | Uniquely identifies an order for internal usage.                                                                                                                      |

Notice of Deprecation

The lowercase field () is deprecated and will be removed in future versions. Use the snake_case versions for consistency.

### Error codes​

| Error code  | Description                                                                                                                                                                                                                                                                                                   |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| UDAPI1010   | **Order id accepts only alphanumeric characters and '-'.** \- The order id you've provided isn't accepted.                                                                                                                                                                                                    |
| UDAPI100059 | **At least one of 'order_id' or 'tag' is required to fetch order details.** \- When attempting to retrieve order details, you must provide either the 'order_id' or the 'tag'. Without at least one of these identifiers, the system cannot locate and present the specific order information you're seeking. |
| UDAPI100010 | **Order not found** \- The system couldn't locate the order you're referring to.                                                                                                                                                                                                                              |

## Examples​

A comprehensive set of examples is provided to illustrate various use cases and implementation scenarios for this API. To view detailed examples and access sample code, please refer to: [API Examples](/developer/api-documentation/example-code/orders/get-order-details).

Loading...

[PreviousCancel Order](/developer/api-documentation/cancel-order)[NextGet Order History](/developer/api-documentation/get-order-history)

---

## [Get Order History | Upstox Developer API](https://upstox.com/developer/api-documentation/get-order-history)

- [](/developer/api-documentation/)
- [Developer API](/developer/api-documentation/open-api)
- [Orders](/developer/api-documentation/orders)
- Get Order History

## Get Order History​

API to retrieve the details of a specific order. Orders placed by the user remain available for one trading day and are automatically removed at the end of the trading session. Provides details regarding the progression of an order through its various execution stages. For a comprehensive list of all possible order statuses, please refer to the [appendix on order status](/developer/api-documentation/appendix/order-status).

Order history can be retrieved by utilizing either the order_id or a tag.

- When both options are provided, the response will include the history of the order that perfectly matches both the order_id and tag.
- If only the tag is provided, the response will include the history of all associated orders that match the given tag.

### Header Parameters​

| Name          | Required | Type   | Description                                                                                         |
| ------------- | -------- | ------ | --------------------------------------------------------------------------------------------------- |
| Authorization | true     | string | Requires the format where is obtained from the [Token API](/developer/api-documentation/get-token). |
| Accept        | true     | string | Defines the content format the client expects, which should be set to .                             |

### Query Parameters​

| Name     | Required | Type   | Description                                                                                                                                                                                            |
| -------- | -------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| order_id | false    | string | The order reference ID for which the order history is required. For the regex pattern applicable to this field, see the [Field Pattern Appendix](/developer/api-documentation/appendix/field-pattern). |
| tag      | false    | string | The unique tag of the order for which the order history is being requested                                                                                                                             |

**Responses**

- 200
- 4XX

---

### Response Body​

| Name            | Type   | Description                                                                                                                                        |
| --------------- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| status          | string | A string indicating the outcome of the request. Typically for successful operations.                                                               |
| data            | object | Response data for order details                                                                                                                    |
| data[].exchange | string | Exchange to which the order is associated. Valid exchanges can be found in the [Exchange Appendix](/developer/api-documentation/appendix/exchange) |
| data[].price    | float  | Price at which the order was placed                                                                                                                |
| data[].product  | string | Signifies if the order was either Intraday, Delivery or CO.                                                                                        |

Possible values: , , , .  
data[].quantity| int32| Quantity with which the order was placed  
data[].status| string| Indicates the current status of the order. Valid order statuses can be found in the [Order Status Appendix](/developer/api-documentation/appendix/order-status)  
data[].tag| string| Tag to uniquely identify an order  
data[].validity| string| It can be one of the following - DAY(default), IOC.  
Possible values: , .  
data[].average_price| float| Average price at which the qty got traded  
data[].disclosed_quantity| int32| The quantity that should be disclosed in the market depth  
data[].exchange_order_id| string| Unique order ID assigned by the exchange for the order placed  
data[].exchange_timestamp| string| User readable time at which the order was placed or updated  
data[].instrument_token| string| Key of the instrument. For the regex pattern applicable to this field, see the [Field Pattern Appendix](/developer/api-documentation/appendix/field-pattern).  
data[].is_amo| boolean| Signifies if the order is an After Market Order  
data[].status_message| string| Indicates the reason when any order is rejected, not modified or cancelled  
data[].order_id| string| Unique order ID assigned internally for the order placed  
data[].order_request_id| string| Apart from 1st order it shows the count of how many requests were sent  
data[].order_type| string| Type of order. It can be one of the following MARKET refers to market order LIMIT refers to Limit Order SL refers to Stop Loss Limit SL-M refers to Stop Loss Market.  
Possible values: , , , .  
data[].parent_order_id| string| In case the order is part of the second of a CO, the parent order ID is indicated here  
data[].trading_symbol| string| Shows the trading symbol of the instrument  
data[].order_timestamp| string| User readable timestamp at which the order was placed  
data[].filled_quantity| int32| The total quantity traded from this particular order  
data[].transaction_type| string| Indicates whether its a buy or sell order.  
Possible values: , .  
data[].trigger_price| float| If the order was a stop loss order then the trigger price set is mentioned here  
data[].placed_by| string| Uniquely identifies the user (commonly referred as UCC)  
data[].variety| string| Order complexity

Notice of Deprecation

The lowercase field () is deprecated and will be removed in future versions. Use the snake_case versions for consistency.

### Error codes​

| Error code  | Description                                                                                                                                                                                                                                                                                                   |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| UDAPI1010   | **Order id accepts only alphanumeric characters and '-'.** \- The order id you've provided isn't accepted.                                                                                                                                                                                                    |
| UDAPI100059 | **At least one of 'order_id' or 'tag' is required to fetch order details.** \- When attempting to retrieve order details, you must provide either the 'order_id' or the 'tag'. Without at least one of these identifiers, the system cannot locate and present the specific order information you're seeking. |
| UDAPI100010 | **Order not found** \- The system couldn't locate the order you're referring to.                                                                                                                                                                                                                              |

## Examples​

A comprehensive set of examples is provided to illustrate various use cases and implementation scenarios for this API. To view detailed examples and access sample code, please refer to: [API Examples](/developer/api-documentation/example-code/orders/get-order-history).

Loading...

[PreviousGet Order Details](/developer/api-documentation/get-order-details)[NextGet Order Book](/developer/api-documentation/get-order-book)

---

## [Get Order Book | Upstox Developer API](https://upstox.com/developer/api-documentation/get-order-book)

- [](/developer/api-documentation/)
- [Developer API](/developer/api-documentation/open-api)
- [Orders](/developer/api-documentation/orders)
- Get Order Book

## Get Order Book​

API to retrieve the list of a orders placed for the current day. Orders initiated by the user remain active for a single day and are automatically cleared at the conclusion of the trading session. The reply indicates the most current status of the order. For a comprehensive list of all possible order statuses, please refer to the [appendix on order status](/developer/api-documentation/appendix/order-status).

### Header Parameters​

| Name          | Required | Type   | Description                                                                                         |
| ------------- | -------- | ------ | --------------------------------------------------------------------------------------------------- |
| Authorization | true     | string | Requires the format where is obtained from the [Token API](/developer/api-documentation/get-token). |
| Accept        | true     | string | Defines the content format the client expects, which should be set to .                             |

**Responses**

- 200

---

### Response Body​

| Name                      | Type    | Description                                                                                                                                                           |
| ------------------------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| status                    | string  | A string indicating the outcome of the request. Typically for successful operations.                                                                                  |
| data                      | object  | Response data for order Book                                                                                                                                          |
| data[].exchange           | string  | Exchange to which the order is associated. Valid exchanges can be found in the [Exchange Appendix](/developer/api-documentation/appendix/exchange)                    |
| data[].product            | string  | Signifies if the order was either Intraday, Delivery or CO.                                                                                                           |
| Possible values: , , , .  |
| data[].price              | float   | Price at which the order was placed                                                                                                                                   |
| data[].quantity           | int32   | Quantity with which the order was placed                                                                                                                              |
| data[].status             | string  | Indicates the current status of the order. Valid order statuses can be found in the [Order Status Appendix](/developer/api-documentation/appendix/order-status)       |
| data[].tag                | string  | Tag to uniquely identify an order                                                                                                                                     |
| data[].instrument_token   | string  | Key of the instrument. For the regex pattern applicable to this field, see the [Field Pattern Appendix](/developer/api-documentation/appendix/field-pattern).         |
| data[].placed_by          | string  | Uniquely identifies the user (commonly referred as UCC)                                                                                                               |
| data[].trading_symbol     | string  | Shows the trading symbol of the instrument                                                                                                                            |
| data[].order_type         | string  | Type of order. It can be one of the following MARKET refers to market order LIMIT refers to Limit Order SL refers to Stop Loss Limit SL-M refers to Stop Loss Market. |
| Possible values: , , , .  |
| data[].validity           | string  | It can be one of the following - DAY(default), IOC.                                                                                                                   |
| Possible values: , .      |
| data[].trigger_price      | float   | If the order was a stop loss order then the trigger price set is mentioned here                                                                                       |
| data[].disclosed_quantity | int32   | The quantity that should be disclosed in the market depth                                                                                                             |
| data[].transaction_type   | string  | Indicates whether its a buy or sell order.                                                                                                                            |
| Possible values: , .      |
| data[].average_price      | float   | Average price at which the qty got traded                                                                                                                             |
| data[].filled_quantity    | int32   | The total quantity traded from this particular order                                                                                                                  |
| data[].pending_quantity   | int32   | Pending quantity to be filled                                                                                                                                         |
| data[].status_message     | string  | Indicates the reason when any order is rejected, not modified or cancelled                                                                                            |
| data[].status_message_raw | string  | Description of the order's status as received from RMS                                                                                                                |
| data[].exchange_order_id  | string  | Unique order ID assigned by the exchange for the order placed                                                                                                         |
| data[].parent_order_id    | string  | In case the order is part of the second of a CO, the parent order ID is indicated here                                                                                |
| data[].order_id           | string  | Unique order ID assigned internally for the order placed                                                                                                              |
| data[].variety            | string  | Order complexity                                                                                                                                                      |
| data[].order_timestamp    | string  | User readable timestamp at which the order was placed                                                                                                                 |
| data[].exchange_timestamp | string  | User readable time at which the order was placed or updated                                                                                                           |
| data[].is_amo             | boolean | Signifies if the order is an After Market Order                                                                                                                       |
| data[].order_request_id   | string  | Apart from 1st order it shows the count of how many requests were sent                                                                                                |
| data[].order_ref_id       | string  | Uniquely identifies an order for internal usage.                                                                                                                      |

Notice of Deprecation

The lowercase field () is deprecated and will be removed in future versions. Use the snake_case versions for consistency.

## Examples​

A comprehensive set of examples is provided to illustrate various use cases and implementation scenarios for this API. To view detailed examples and access sample code, please refer to: [API Examples](/developer/api-documentation/example-code/orders/get-order-book).

Loading...

[PreviousGet Order History](/developer/api-documentation/get-order-history)[NextGet Trades](/developer/api-documentation/get-trade-history)

---

## [API Structure | Upstox Developer API](https://upstox.com/developer/api-documentation/request-response#docusaurus_skipToContent_fallback)

- [](/developer/api-documentation/)
- [Developer API](/developer/api-documentation/open-api)
- API Structure

# API Structure

## [description Request StructureOverview of the request structure.](/developer/api-documentation/request-structure)## [description Response StructureOverview of the response structure.](/developer/api-documentation/response-structure)## [description Error CodesDescription of the error codes.](/developer/api-documentation/error-codes)

[PreviousAuthentication](/developer/api-documentation/authentication)[NextRequest Structure](/developer/api-documentation/request-structure)

---

## [Request Structure | Upstox Developer API](https://upstox.com/developer/api-documentation/request-structure)

- [](/developer/api-documentation/)
- [Developer API](/developer/api-documentation/open-api)
- [API Structure](/developer/api-documentation/request-response)
- Request Structure

# Request Structure

Use the following structure to make requests to the Upstox API:

Placeholders:

| Name                  | Description                                                                                                                                 |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| [API_METHOD]          | The HTTP method for your request (e.g., GET, POST, PUT, DELETE).                                                                            |
| [API_ENDPOINT]        | The specific endpoint you're targeting (e.g., /user/profile, /order/place).                                                                 |
| [YOUR_ACCESS_TOKEN]   | Your personal access token for authentication.                                                                                              |
| [CONTENT_TYPE_HEADER] | Include -H for requests that send a JSON payload. Include -H for requests that send data in key-value pair format. Omit for other requests. |
| [REQUEST_PAYLOAD]     | For POST and PUT methods that send data, use . Omit for other methods.                                                                      |

Note

All API requests must be encoded using the **Standard URL Encoding** \- Encodes special characters and non-ASCII characters using the percent sign and two hexadecimal digits.

[PreviousAPI Structure](/developer/api-documentation/request-response)[NextResponse Structure](/developer/api-documentation/response-structure)

---

## [Response Structure | Upstox Developer API](https://upstox.com/developer/api-documentation/response-structure)

- [](/developer/api-documentation/)
- [Developer API](/developer/api-documentation/open-api)
- [API Structure](/developer/api-documentation/request-response)
- Response Structure

On this page

# Response Structure

## Success response​

### Single Object Response Structure​

Used for endpoints that return a single object, like and .

### Multiple Object Response Structure​

Used for endpoints that return a multiple object, like

Properties:

| Property | Description                                                                          |
| -------- | ------------------------------------------------------------------------------------ |
| status   | A string indicating the outcome of the request. Typically for successful operations. |
| data     | An object holding the response content with various key-value pairs.                 |

An array containing the main content of the response. Each element of the array is an object with various key-value pairs.

## Error response​

Properties:

| Property      | Description                                                                                                      |
| ------------- | ---------------------------------------------------------------------------------------------------------------- |
| status        | A string indicating the outcome of the request. In this context, the term represents a failure in the operation. |
| errors        | An array containing the main content of the error response.                                                      |
| error_code    | A specific error. Refer to the "Error Code" section for explanations.                                            |
| message       | Descriptive error message.                                                                                       |
| property_path | Indicates which part of the request triggered the error. It can be null.                                         |
| invalid_value | Shows the value causing the error. It can be null.                                                               |

Notice of Deprecation

The camelCase fields (, , and ) are deprecated and will be removed in future versions. Use the snake_case versions for consistency.

[PreviousRequest Structure](/developer/api-documentation/request-structure)[NextError Codes](/developer/api-documentation/error-codes)

- Success response
  - Single Object Response Structure
  - Multiple Object Response Structure
- Error response

---

## [Error codes | Upstox Developer API](https://upstox.com/developer/api-documentation/error-codes)

- [](/developer/api-documentation/)
- [Developer API](/developer/api-documentation/open-api)
- [API Structure](/developer/api-documentation/request-response)
- Error Codes

On this page

# Error Codes

## HTTP error codes​

| Error code            | Description                                                        |
| --------------------- | ------------------------------------------------------------------ |
| Bad Request           | Your request parameters are incorrect.                             |
| Unauthorized          | Your API key is wrong or missing.                                  |
| Forbidden             | The requested resource is hidden for administrators only.          |
| Not Found             | The specified resource could not be found.                         |
| Method Not Allowed    | You tried to access a resource with an invalid method.             |
| Not Acceptable        | You requested a format that isn’t json.                            |
| Gone                  | The resource requested has been removed from our servers.          |
| Too Many Requests     | You’re requesting too many resources! Slow down!                   |
| Internal Server Error | We had a problem with our server. Please try again later.          |
| Service Unavailable   | We’re temporarily offline for maintenance. Please try again later. |

## Common API error codes​

| Error code  | Description                                                                                                                                                                                                         |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| UDAPI10000  | **This request is not supported by Upstox API** \- This error is thrown when the API call is not recognized or valid, possibly due to incorrect URL formatting or the presence of unexpected characters in the URL. |
| UDAPI100016 | **Invalid Credentials** \- Thrown when one of the credentials you've passed to this API is invalid.                                                                                                                 |
| UDAPI10005  | **Too Many Request Sent** \- Thrown when you've exceeded the Rate limits for the API.                                                                                                                               |
| UDAPI100015 | **API Version does not exist** \- Thrown when API version isn't part of the Header attributes.                                                                                                                      |
| UDAPI100050 | **Invalid token used to access API** \- Thrown when an invalid token is used to access the API.                                                                                                                     |
| UDAPI100067 | **The API you are trying to access is not permitted with an extended_token** \- Thrown when trying to access an API that is not allowed with an extended_token.                                                     |
| UDAPI100036 | **Invalid Input** \- Thrown when an invalid input is passed to the API.                                                                                                                                             |
| UDAPI100038 | **Invalid input passed to the API** \- Thrown when an invalid input is passed to the API.                                                                                                                           |
| UDAPI100073 | **Your 'client_id' is inactive.** \- Thrown when the is not active. Please contact the support team for further assistance.                                                                                         |
| UDAPI100500 | **Something went wrong... please contact us** \- An unexpected error occurred. Please contact support.                                                                                                              |

Error codes specific to each API are detailed in the **4XX** response section within their respective documentation.

[PreviousResponse Structure](/developer/api-documentation/response-structure)[NextRate Limits](/developer/api-documentation/rate-limiting)

- HTTP error codes
- Common API error codes

---

## [Rate Limits | Upstox Developer API](https://upstox.com/developer/api-documentation/rate-limiting#docusaurus_skipToContent_fallback)

- [](/developer/api-documentation/)
- [Developer API](/developer/api-documentation/open-api)
- Rate Limits

# Rate Limits

In our pursuit of offering a consistent and reliable service, we've established rate limits for our API interactions. These constraints, detailed below, are designed to prevent system overloads and ensure equitable access to all our users. The rate limits are enforced on a per-API, per-user basis.

| Time duration  | Request limit |
| -------------- | ------------- |
| Per second     | 25 requests   |
| Per minute     | 250 requests  |
| Per 30 minutes | 1000 requests |

NOTE

Please adhere to these limits to avoid potential disruptions in service. Exceeding these limits might result in temporary suspension of access.

[PreviousError Codes](/developer/api-documentation/error-codes)[NextSDK](/developer/api-documentation/sdk)

---

## [SDK | Upstox Developer API](https://upstox.com/developer/api-documentation/sdk#docusaurus_skipToContent_fallback)

- [](/developer/api-documentation/)
- [Developer API](/developer/api-documentation/open-api)
- SDK

# SDK

## [description Upstox GeneratedGet started with Upstox generated SDK for Python, PHP, NodeJS, Java and .NET](/developer/api-documentation/upstox-generated-sdk)## [description Self GeneratedGenerate SDK in your preferred language.](/developer/api-documentation/self-generated-sdk)

[PreviousRate Limits](/developer/api-documentation/rate-limiting)[NextUpstox Generated](/developer/api-documentation/upstox-generated-sdk)

---

## [Upstox Generated SDK's | Upstox Developer API](https://upstox.com/developer/api-documentation/upstox-generated-sdk)

- [](/developer/api-documentation/)
- [Developer API](/developer/api-documentation/open-api)
- [SDK](/developer/api-documentation/sdk)
- Upstox Generated

On this page

# Upstox Generated SDK's

## Python​

Repository: [](https://github.com/upstox/upstox-python)

NOTE

Fields in the SDK follow snake_case formatting, e.g., , .

## PHP​

Repository: [](https://github.com/upstox/upstox-php)

NOTE

Fields in the SDK follow snake_case formatting, e.g., , .

## NodeJS​

Repository: [](https://github.com/upstox/upstox-nodejs)

    **Node.js Code:**

    **Node.js Code:**

     npm install upstox-js-sdk

NOTE

Fields in the SDK follow camelCase formatting, e.g., , .

## Java​

Repository: [](https://github.com/upstox/upstox-java)

Include the following Maven dependency:

NOTE

Fields in the SDK follow camelCase formatting, e.g., , .

## .NET​

Repository: [](https://github.com/upstox/upstox-dotnet)

NOTE

Fields in the SDK follow PascalCase formatting, e.g., , .

## Transition Guide for Upcoming SDK Field Deprecations​

As part of our ongoing efforts to improve the Upstox SDK, we are introducing alternate fields to replace those that will soon be deprecated. This change is designed to ensure a smoother transition and maintain the consistency of your applications. We encourage you to start using the recommended fields listed below. Both the deprecated and the new fields will be available for some time to facilitate this transition. However, please note that deprecated fields will eventually be removed. For detailed information on which fields are being deprecated, refer to the respective API documentation.

| API Field to be Deprecated | SDK Field to be Deprecated | Recommended SDK Field to Use | Language | APIs     |
| -------------------------- | -------------------------- | ---------------------------- | -------- | -------- |
| tradingsymbol              | tradingsymbol              | trading_symbol               | Python   | Multiple |
| tradingsymbol              | trading_symbol             | PHP                          | Multiple |
| tradingsymbol              | tradingSymbol              | NodeJS                       | Multiple |
| tradingsymbol              | tradingSymbol              | Java                         | Multiple |
| Tradingsymbol              | TradingSymbol              | .NET                         | Multiple |

Note

In instances where a field is utilized in multiple APIs, we recommend searching through the entire documentation to identify all the APIs that make use of this field.

[PreviousSDK](/developer/api-documentation/sdk)[NextSelf Generated](/developer/api-documentation/self-generated-sdk)

- Python
- PHP
- NodeJS
- Java
- .NET
- Transition Guide for Upcoming SDK Field Deprecations

---

## [Self Generated SDK's | Upstox Developer API](https://upstox.com/developer/api-documentation/self-generated-sdk)

- [](/developer/api-documentation/)
- [Developer API](/developer/api-documentation/open-api)
- [SDK](/developer/api-documentation/sdk)
- Self Generated

On this page

# Self Generated SDK's

Our SDK generation flow offers the capability to craft SDKs in over 10 distinct languages. This feature ensures you're equipped with the flexibility to produce SDKs tailored to your precise requirements.

## Get Upstox developer API YAML​

Download the yaml file from the following link: <https://api.upstox.com/v2/api-docs>

## Offline SDK generation using swagger-codegen-cli​

### Windows​

- Download the latest jar file from <https://mvnrepository.com/artifact/io.swagger.codegen.v3/swagger-codegen-cli>.

NOTE

OpenAPI 3.0 is supported only from swagger-codegen-cli-3.x versions.

- Execute the below command to generate the client in a preferred language.

  - Using online api docs

  - Using yaml file

### MAC​

- Execute the below command on Mac terminal to download swagger codegen

- To generate the client in preferred language.

  - Using online api docs

  - Using yaml file

tip

-h, --help show this help message and exit.  
-l, --lang client language to generate.  
-o, --output where to write the generated files (current dir by default).  
-i, --input-spec location of the swagger spec, as URL or file (required).

## Online SDK generation using swagger editor​

- Open your favourite browser and visit [swagger editor](https://editor.swagger.io/).
- Under the File menu, select the Import file option. ![Swagger import file](/developer/api-documentation/assets/images/onlinesdk1-1879afec7bcdacbb01d4fd370ae968da.webp)
- Import the downloaded yaml from first section yaml.
- Click on generate client. ![Swagger import file](/developer/api-documentation/assets/images/onlinesdk2-6220df7e50da5e32cd228497d9d6a283.webp)
- Choose language from options provided. ![Swagger import file](/developer/api-documentation/assets/images/onlinesdk3-0f3e501970f3ad5b6e24bd5262f3d2f0.webp)
- A zip file will be downloaded.
- Extract the zip to use your SDK.
- Each SDK comes with readme file to know how to install and use SDK.

[PreviousUpstox Generated](/developer/api-documentation/upstox-generated-sdk)[NextInstruments](/developer/api-documentation/instruments)

- Get Upstox developer API YAML
- Offline SDK generation using swagger-codegen-cli
  - Windows
  - MAC
- Online SDK generation using swagger editor

---

## [Instruments | Upstox Developer API](https://upstox.com/developer/api-documentation/instruments#docusaurus_skipToContent_fallback)

- [](/developer/api-documentation/)
- [Developer API](/developer/api-documentation/open-api)
- Instruments

On this page

# Instruments

Note

- **The CSV format for instruments files is being deprecated.** Switch to the JSON format for improved performance. Details at [CSV Instruments File Deprecation Notice](/developer/api-documentation/announcements/instruments-csv-deprecation-notice).
- The list of suspended instruments is available in the [JSON section](/developer/api-documentation/instruments#json-files) below.

Recommendations

- Use for uniquely identifying instruments, as it remains unique for each instrument. Conversely, may be reused by the exchange for a different instrument after its expiry.
- Use Instruments data in JSON format instead of CSV, as its structure has been designed for enhanced robustness and future scalability, making programmatic processing easier.

## CSV Files​

These URLs provide access to the complete list of BOD contracts available for trading on Upstox in CSV format.

- [Complete](https://assets.upstox.com/market-quote/instruments/exchange/complete.csv.gz)
- [NSE](https://assets.upstox.com/market-quote/instruments/exchange/NSE.csv.gz)
- [BSE](https://assets.upstox.com/market-quote/instruments/exchange/BSE.csv.gz)
- [MCX](https://assets.upstox.com/market-quote/instruments/exchange/MCX.csv.gz)

### Sample CSV Record​

| instrument_key | exchange_token | tradingsymbol | name                | last_price              | expiry | strike     | tick_size | lot_size | instrument_type | option_type | exchange |
| -------------- | -------------- | ------------- | ------------------- | ----------------------- | ------ | ---------- | --------- | -------- | --------------- | ----------- | -------- | ------ |
| NSE_FO         | 164693         | 164693        | RELIANCE24JAN1840CE | RELIANCE INDUSTRIES LTD | 424.8  | 2024-01-25 | 1840.0    | 0.05     | 250             | OPTSTK      | CE       | NSE_FO |

### Field Description​

| Name            | Type   | Description                                                                                                                                                                                                                                                          |
| --------------- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| instrument_key  | string | The unique identifier used across Upstox APIs for instrument identification. For the regex pattern applicable to this field, see the [Field Pattern Appendix](/developer/api-documentation/appendix/field-pattern).                                                  |
| exchange_token  | number | The numerical identifier issued by the exchange representing the instrument.                                                                                                                                                                                         |
| tradingsymbol   | string | Shows the trading symbol which could be a combination of symbol name, instrument, expiry date etc. The format of this value may vary between weekly and monthly contracts, leading to inconsistencies. These inconsistencies have been resolved in the JSON version. |
| name            | string | Name of the company (for equity instruments).                                                                                                                                                                                                                        |
| last_price      | number | Last traded price.                                                                                                                                                                                                                                                   |
| expiry          | string | Expiry date (for derivatives). Data format is                                                                                                                                                                                                                        |
| strike          | number | Indicates the predetermined price at which an option can be bought or sold when it's exercised.                                                                                                                                                                      |
| tick_size       | number | Measure of the minimum upward or downward movement in the price of an instrument.                                                                                                                                                                                    |
| lot_size        | number | Minimum size in which the stock futures or index futures can be traded.                                                                                                                                                                                              |
| instrument_type | string | Instrument type of a particular contract.                                                                                                                                                                                                                            |

Possible values: , , etc.  
option_type| string| Option type of the option contracts (applicable only for options contract).  
Possible values: ,  
exchange| string| Exchange to which the order is associated.  
Possible values: , , , , , etc.

## JSON files​

These URLs provide access to the complete list of BOD contracts available for trading on Upstox in JSON format.

- [Complete](https://assets.upstox.com/market-quote/instruments/exchange/complete.json.gz)
- [NSE](https://assets.upstox.com/market-quote/instruments/exchange/NSE.json.gz)
- [BSE](https://assets.upstox.com/market-quote/instruments/exchange/BSE.json.gz)
- [MCX](https://assets.upstox.com/market-quote/instruments/exchange/MCX.json.gz)
- [Suspended](https://assets.upstox.com/market-quote/instruments/exchange/suspended-instrument.json.gz)

### Sample JSON Object​

- EQ
- Futures
- Options
- INDEX

Note

- When you're searching for instrument keys within an instrument JSON file, you can employ the and parameters to refine and narrow down the list of instrument keys. For instance, if you're looking for the instrument key for Reliance Equity, specify the as and the as , excluding other segments and instrument types from your search criteria.

### Field Description

| Field Name | Type   | Description                                    |
| ---------- | ------ | ---------------------------------------------- |
| segment    | string | Segment to which the instrument is associated. |

Possible values: , , , , , , , ,  
name| string| The name of the equity.  
exchange| string| Exchange to which the instrument is associated.  
Possible values: , ,  
isin| string| The International Securities Identification Number.  
instrument_type| string| The instrument types for NSE are present at [NSE India](https://www.nseindia.com/market-data/legend-of-series) and for BSE are present at [BSE India](https://www.bseindia.com/markets/equity/EQReports/tra_trading.aspx).  
instrument_key| string| The unique identifier used across Upstox APIs for instrument identification. For the regex pattern applicable to this field, see the [Field Pattern Appendix](/developer/api-documentation/appendix/field-pattern).  
lot_size| number| The size of one lot of the equity.  
freeze_quantity| number| The maximum quantity that can be frozen.  
exchange_token| string| The exchange-specific token for the equity.  
tick_size| number| The minimum price movement of the equity.  
trading_symbol| string| Trading symbol of the instrument.  
short_name| string| A shorter or abbreviated name of the equity.  
security_type| string| Identifies the classification or status of a security within the market. Valid security types can be found in the [Security Type Appendix](/developer/api-documentation/appendix/equity-security-type)

Note

- When you're searching for instrument keys within an instrument JSON file, you can employ the and parameters to refine and narrow down the list of instrument keys. For instance, if you're looking for the instrument key for Reliance Future, specify the as and the as , excluding other segments and instrument types from your search criteria.

### Field Description

| Field Name        | Type    | Description                                                                                                                                                                                                         |
| ----------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| weekly            | boolean | Indicates if the future is weekly.                                                                                                                                                                                  |
| segment           | string  | Segment to which the instrument is associated. Possible values: , , , , , , , ,                                                                                                                                     |
| name              | string  | The name of the future.                                                                                                                                                                                             |
| exchange          | string  | Exchange to which the instrument is associated. Possible values: , ,                                                                                                                                                |
| expiry            | date    | The expiry date of the future.                                                                                                                                                                                      |
| instrument_type   | string  | The type of the future instrument. Possible values:                                                                                                                                                                 |
| underlying_symbol | string  | The symbol of the underlying asset.                                                                                                                                                                                 |
| instrument_key    | string  | The unique identifier used across Upstox APIs for instrument identification. For the regex pattern applicable to this field, see the [Field Pattern Appendix](/developer/api-documentation/appendix/field-pattern). |
| lot_size          | number  | The size of one lot of the future.                                                                                                                                                                                  |
| freeze_quantity   | number  | The maximum quantity that can be frozen.                                                                                                                                                                            |
| exchange_token    | string  | The exchange-specific token for the future.                                                                                                                                                                         |
| minimum_lot       | number  | The minimum lot size for the future.                                                                                                                                                                                |
| underlying_key    | string  | The for the underlying asset.                                                                                                                                                                                       |
| tick_size         | number  | The minimum price movement of the future.                                                                                                                                                                           |
| underlying_type   | string  | The type of the underlying asset. Possible values: , , , ,                                                                                                                                                          |
| trading_symbol    | string  | The symbol used for trading the future. Format:                                                                                                                                                                     |

Note

- When you're searching for instrument keys within an instrument JSON file, you can employ the and parameters to refine and narrow down the list of instrument keys. For instance, if you're looking for the instrument key for Reliance Call Option, specify the as and the as , excluding other segments and instrument types from your search criteria. If you want to search for Put Option then set as .

### Field Description

| Field Name        | Type    | Description                                                                                                                                                                                                         |
| ----------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| weekly            | boolean | Indicates if the option is weekly.                                                                                                                                                                                  |
| segment           | string  | The market segment of the option. Possible values: , , , , , , , ,                                                                                                                                                  |
| name              | string  | The name of the option.                                                                                                                                                                                             |
| exchange          | string  | Exchange to which the instrument is associated. Possible values: , ,                                                                                                                                                |
| expiry            | date    | The expiry date of the option.                                                                                                                                                                                      |
| instrument_type   | string  | The type of the option instrument. Possible values: ,                                                                                                                                                               |
| underlying_symbol | string  | The symbol of the underlying asset.                                                                                                                                                                                 |
| instrument_key    | string  | The unique identifier used across Upstox APIs for instrument identification. For the regex pattern applicable to this field, see the [Field Pattern Appendix](/developer/api-documentation/appendix/field-pattern). |
| strike_price      | number  | The strike price for the option.                                                                                                                                                                                    |
| lot_size          | number  | The size of one lot of the option.                                                                                                                                                                                  |
| freeze_quantity   | number  | The maximum quantity that can be frozen.                                                                                                                                                                            |
| exchange_token    | string  | The exchange-specific token for the option.                                                                                                                                                                         |
| minimum_lot       | number  | The minimum lot size for the option.                                                                                                                                                                                |
| underlying_key    | string  | The for the underlying asset.                                                                                                                                                                                       |
| tick_size         | number  | The minimum price movement of the option.                                                                                                                                                                           |
| underlying_type   | string  | The type of the underlying asset. Possible values: , , , ,                                                                                                                                                          |
| trading_symbol    | string  | The symbol used for trading the option. Format:                                                                                                                                                                     |

Note

- When you're searching for instrument keys within an instrument JSON file, you can employ the and parameters to refine and narrow down the list of instrument keys. For instance, if you're looking for the instrument key for NSE Index, specify the as and the as , excluding other segments and instrument types from your search criteria.

### Field Description​

| Field Name | Type   | Description                                    |
| ---------- | ------ | ---------------------------------------------- |
| segment    | string | Segment to which the instrument is associated. |

Possible values: , , , , , , , ,  
name| string| The name of the index.  
exchange| string| Exchange to which the instrument is associated.  
Possible values: , ,  
instrument_type| string| The type of the option instrument.  
Possible values:  
instrument_key| string| The unique identifier used across Upstox APIs for instrument identification. For the regex pattern applicable to this field, see the [Field Pattern Appendix](/developer/api-documentation/appendix/field-pattern).  
exchange_token| number| The numerical identifier issued by the exchange representing the instrument.  
trading_symbol| string| Trading symbol for the index.

Note

- The files undergo daily refresh at around 6 AM, and they are only refreshed as needed during the day, which is a seldom occurrence.
- The BOD instrument for the next trading day will not include delisted stocks or expired contracts.

[PreviousSelf Generated](/developer/api-documentation/self-generated-sdk)[NextLogin](/developer/api-documentation/login)

- CSV Files
  - Sample CSV Record
  - Field Description
- JSON files
  - Sample JSON Object
  - Field Description

---

## [Instruments | Upstox Developer API](https://upstox.com/developer/api-documentation/instruments#sample-csv-record)

- [](/developer/api-documentation/)
- [Developer API](/developer/api-documentation/open-api)
- Instruments

On this page

# Instruments

Note

- **The CSV format for instruments files is being deprecated.** Switch to the JSON format for improved performance. Details at [CSV Instruments File Deprecation Notice](/developer/api-documentation/announcements/instruments-csv-deprecation-notice).
- The list of suspended instruments is available in the [JSON section](/developer/api-documentation/instruments#json-files) below.

Recommendations

- Use for uniquely identifying instruments, as it remains unique for each instrument. Conversely, may be reused by the exchange for a different instrument after its expiry.
- Use Instruments data in JSON format instead of CSV, as its structure has been designed for enhanced robustness and future scalability, making programmatic processing easier.

## CSV Files​

These URLs provide access to the complete list of BOD contracts available for trading on Upstox in CSV format.

- [Complete](https://assets.upstox.com/market-quote/instruments/exchange/complete.csv.gz)
- [NSE](https://assets.upstox.com/market-quote/instruments/exchange/NSE.csv.gz)
- [BSE](https://assets.upstox.com/market-quote/instruments/exchange/BSE.csv.gz)
- [MCX](https://assets.upstox.com/market-quote/instruments/exchange/MCX.csv.gz)

### Sample CSV Record​

| instrument_key | exchange_token | tradingsymbol | name                | last_price              | expiry | strike     | tick_size | lot_size | instrument_type | option_type | exchange |
| -------------- | -------------- | ------------- | ------------------- | ----------------------- | ------ | ---------- | --------- | -------- | --------------- | ----------- | -------- | ------ |
| NSE_FO         | 164693         | 164693        | RELIANCE24JAN1840CE | RELIANCE INDUSTRIES LTD | 424.8  | 2024-01-25 | 1840.0    | 0.05     | 250             | OPTSTK      | CE       | NSE_FO |

### Field Description​

| Name            | Type   | Description                                                                                                                                                                                                                                                          |
| --------------- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| instrument_key  | string | The unique identifier used across Upstox APIs for instrument identification. For the regex pattern applicable to this field, see the [Field Pattern Appendix](/developer/api-documentation/appendix/field-pattern).                                                  |
| exchange_token  | number | The numerical identifier issued by the exchange representing the instrument.                                                                                                                                                                                         |
| tradingsymbol   | string | Shows the trading symbol which could be a combination of symbol name, instrument, expiry date etc. The format of this value may vary between weekly and monthly contracts, leading to inconsistencies. These inconsistencies have been resolved in the JSON version. |
| name            | string | Name of the company (for equity instruments).                                                                                                                                                                                                                        |
| last_price      | number | Last traded price.                                                                                                                                                                                                                                                   |
| expiry          | string | Expiry date (for derivatives). Data format is                                                                                                                                                                                                                        |
| strike          | number | Indicates the predetermined price at which an option can be bought or sold when it's exercised.                                                                                                                                                                      |
| tick_size       | number | Measure of the minimum upward or downward movement in the price of an instrument.                                                                                                                                                                                    |
| lot_size        | number | Minimum size in which the stock futures or index futures can be traded.                                                                                                                                                                                              |
| instrument_type | string | Instrument type of a particular contract.                                                                                                                                                                                                                            |

Possible values: , , etc.  
option_type| string| Option type of the option contracts (applicable only for options contract).  
Possible values: ,  
exchange| string| Exchange to which the order is associated.  
Possible values: , , , , , etc.

## JSON files​

These URLs provide access to the complete list of BOD contracts available for trading on Upstox in JSON format.

- [Complete](https://assets.upstox.com/market-quote/instruments/exchange/complete.json.gz)
- [NSE](https://assets.upstox.com/market-quote/instruments/exchange/NSE.json.gz)
- [BSE](https://assets.upstox.com/market-quote/instruments/exchange/BSE.json.gz)
- [MCX](https://assets.upstox.com/market-quote/instruments/exchange/MCX.json.gz)
- [Suspended](https://assets.upstox.com/market-quote/instruments/exchange/suspended-instrument.json.gz)

### Sample JSON Object​

- EQ
- Futures
- Options
- INDEX

Note

- When you're searching for instrument keys within an instrument JSON file, you can employ the and parameters to refine and narrow down the list of instrument keys. For instance, if you're looking for the instrument key for Reliance Equity, specify the as and the as , excluding other segments and instrument types from your search criteria.

### Field Description

| Field Name | Type   | Description                                    |
| ---------- | ------ | ---------------------------------------------- |
| segment    | string | Segment to which the instrument is associated. |

Possible values: , , , , , , , ,  
name| string| The name of the equity.  
exchange| string| Exchange to which the instrument is associated.  
Possible values: , ,  
isin| string| The International Securities Identification Number.  
instrument_type| string| The instrument types for NSE are present at [NSE India](https://www.nseindia.com/market-data/legend-of-series) and for BSE are present at [BSE India](https://www.bseindia.com/markets/equity/EQReports/tra_trading.aspx).  
instrument_key| string| The unique identifier used across Upstox APIs for instrument identification. For the regex pattern applicable to this field, see the [Field Pattern Appendix](/developer/api-documentation/appendix/field-pattern).  
lot_size| number| The size of one lot of the equity.  
freeze_quantity| number| The maximum quantity that can be frozen.  
exchange_token| string| The exchange-specific token for the equity.  
tick_size| number| The minimum price movement of the equity.  
trading_symbol| string| Trading symbol of the instrument.  
short_name| string| A shorter or abbreviated name of the equity.  
security_type| string| Identifies the classification or status of a security within the market. Valid security types can be found in the [Security Type Appendix](/developer/api-documentation/appendix/equity-security-type)

Note

- When you're searching for instrument keys within an instrument JSON file, you can employ the and parameters to refine and narrow down the list of instrument keys. For instance, if you're looking for the instrument key for Reliance Future, specify the as and the as , excluding other segments and instrument types from your search criteria.

### Field Description

| Field Name        | Type    | Description                                                                                                                                                                                                         |
| ----------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| weekly            | boolean | Indicates if the future is weekly.                                                                                                                                                                                  |
| segment           | string  | Segment to which the instrument is associated. Possible values: , , , , , , , ,                                                                                                                                     |
| name              | string  | The name of the future.                                                                                                                                                                                             |
| exchange          | string  | Exchange to which the instrument is associated. Possible values: , ,                                                                                                                                                |
| expiry            | date    | The expiry date of the future.                                                                                                                                                                                      |
| instrument_type   | string  | The type of the future instrument. Possible values:                                                                                                                                                                 |
| underlying_symbol | string  | The symbol of the underlying asset.                                                                                                                                                                                 |
| instrument_key    | string  | The unique identifier used across Upstox APIs for instrument identification. For the regex pattern applicable to this field, see the [Field Pattern Appendix](/developer/api-documentation/appendix/field-pattern). |
| lot_size          | number  | The size of one lot of the future.                                                                                                                                                                                  |
| freeze_quantity   | number  | The maximum quantity that can be frozen.                                                                                                                                                                            |
| exchange_token    | string  | The exchange-specific token for the future.                                                                                                                                                                         |
| minimum_lot       | number  | The minimum lot size for the future.                                                                                                                                                                                |
| underlying_key    | string  | The for the underlying asset.                                                                                                                                                                                       |
| tick_size         | number  | The minimum price movement of the future.                                                                                                                                                                           |
| underlying_type   | string  | The type of the underlying asset. Possible values: , , , ,                                                                                                                                                          |
| trading_symbol    | string  | The symbol used for trading the future. Format:                                                                                                                                                                     |

Note

- When you're searching for instrument keys within an instrument JSON file, you can employ the and parameters to refine and narrow down the list of instrument keys. For instance, if you're looking for the instrument key for Reliance Call Option, specify the as and the as , excluding other segments and instrument types from your search criteria. If you want to search for Put Option then set as .

### Field Description

| Field Name        | Type    | Description                                                                                                                                                                                                         |
| ----------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| weekly            | boolean | Indicates if the option is weekly.                                                                                                                                                                                  |
| segment           | string  | The market segment of the option. Possible values: , , , , , , , ,                                                                                                                                                  |
| name              | string  | The name of the option.                                                                                                                                                                                             |
| exchange          | string  | Exchange to which the instrument is associated. Possible values: , ,                                                                                                                                                |
| expiry            | date    | The expiry date of the option.                                                                                                                                                                                      |
| instrument_type   | string  | The type of the option instrument. Possible values: ,                                                                                                                                                               |
| underlying_symbol | string  | The symbol of the underlying asset.                                                                                                                                                                                 |
| instrument_key    | string  | The unique identifier used across Upstox APIs for instrument identification. For the regex pattern applicable to this field, see the [Field Pattern Appendix](/developer/api-documentation/appendix/field-pattern). |
| strike_price      | number  | The strike price for the option.                                                                                                                                                                                    |
| lot_size          | number  | The size of one lot of the option.                                                                                                                                                                                  |
| freeze_quantity   | number  | The maximum quantity that can be frozen.                                                                                                                                                                            |
| exchange_token    | string  | The exchange-specific token for the option.                                                                                                                                                                         |
| minimum_lot       | number  | The minimum lot size for the option.                                                                                                                                                                                |
| underlying_key    | string  | The for the underlying asset.                                                                                                                                                                                       |
| tick_size         | number  | The minimum price movement of the option.                                                                                                                                                                           |
| underlying_type   | string  | The type of the underlying asset. Possible values: , , , ,                                                                                                                                                          |
| trading_symbol    | string  | The symbol used for trading the option. Format:                                                                                                                                                                     |

Note

- When you're searching for instrument keys within an instrument JSON file, you can employ the and parameters to refine and narrow down the list of instrument keys. For instance, if you're looking for the instrument key for NSE Index, specify the as and the as , excluding other segments and instrument types from your search criteria.

### Field Description​

| Field Name | Type   | Description                                    |
| ---------- | ------ | ---------------------------------------------- |
| segment    | string | Segment to which the instrument is associated. |

Possible values: , , , , , , , ,  
name| string| The name of the index.  
exchange| string| Exchange to which the instrument is associated.  
Possible values: , ,  
instrument_type| string| The type of the option instrument.  
Possible values:  
instrument_key| string| The unique identifier used across Upstox APIs for instrument identification. For the regex pattern applicable to this field, see the [Field Pattern Appendix](/developer/api-documentation/appendix/field-pattern).  
exchange_token| number| The numerical identifier issued by the exchange representing the instrument.  
trading_symbol| string| Trading symbol for the index.

Note

- The files undergo daily refresh at around 6 AM, and they are only refreshed as needed during the day, which is a seldom occurrence.
- The BOD instrument for the next trading day will not include delisted stocks or expired contracts.

[PreviousSelf Generated](/developer/api-documentation/self-generated-sdk)[NextLogin](/developer/api-documentation/login)

- CSV Files
  - Sample CSV Record
  - Field Description
- JSON files
  - Sample JSON Object
  - Field Description

---

## [Instruments | Upstox Developer API](https://upstox.com/developer/api-documentation/instruments#field-description)

- [](/developer/api-documentation/)
- [Developer API](/developer/api-documentation/open-api)
- Instruments

On this page

# Instruments

Note

- **The CSV format for instruments files is being deprecated.** Switch to the JSON format for improved performance. Details at [CSV Instruments File Deprecation Notice](/developer/api-documentation/announcements/instruments-csv-deprecation-notice).
- The list of suspended instruments is available in the [JSON section](/developer/api-documentation/instruments#json-files) below.

Recommendations

- Use for uniquely identifying instruments, as it remains unique for each instrument. Conversely, may be reused by the exchange for a different instrument after its expiry.
- Use Instruments data in JSON format instead of CSV, as its structure has been designed for enhanced robustness and future scalability, making programmatic processing easier.

## CSV Files​

These URLs provide access to the complete list of BOD contracts available for trading on Upstox in CSV format.

- [Complete](https://assets.upstox.com/market-quote/instruments/exchange/complete.csv.gz)
- [NSE](https://assets.upstox.com/market-quote/instruments/exchange/NSE.csv.gz)
- [BSE](https://assets.upstox.com/market-quote/instruments/exchange/BSE.csv.gz)
- [MCX](https://assets.upstox.com/market-quote/instruments/exchange/MCX.csv.gz)

### Sample CSV Record​

| instrument_key | exchange_token | tradingsymbol | name                | last_price              | expiry | strike     | tick_size | lot_size | instrument_type | option_type | exchange |
| -------------- | -------------- | ------------- | ------------------- | ----------------------- | ------ | ---------- | --------- | -------- | --------------- | ----------- | -------- | ------ |
| NSE_FO         | 164693         | 164693        | RELIANCE24JAN1840CE | RELIANCE INDUSTRIES LTD | 424.8  | 2024-01-25 | 1840.0    | 0.05     | 250             | OPTSTK      | CE       | NSE_FO |

### Field Description​

| Name            | Type   | Description                                                                                                                                                                                                                                                          |
| --------------- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| instrument_key  | string | The unique identifier used across Upstox APIs for instrument identification. For the regex pattern applicable to this field, see the [Field Pattern Appendix](/developer/api-documentation/appendix/field-pattern).                                                  |
| exchange_token  | number | The numerical identifier issued by the exchange representing the instrument.                                                                                                                                                                                         |
| tradingsymbol   | string | Shows the trading symbol which could be a combination of symbol name, instrument, expiry date etc. The format of this value may vary between weekly and monthly contracts, leading to inconsistencies. These inconsistencies have been resolved in the JSON version. |
| name            | string | Name of the company (for equity instruments).                                                                                                                                                                                                                        |
| last_price      | number | Last traded price.                                                                                                                                                                                                                                                   |
| expiry          | string | Expiry date (for derivatives). Data format is                                                                                                                                                                                                                        |
| strike          | number | Indicates the predetermined price at which an option can be bought or sold when it's exercised.                                                                                                                                                                      |
| tick_size       | number | Measure of the minimum upward or downward movement in the price of an instrument.                                                                                                                                                                                    |
| lot_size        | number | Minimum size in which the stock futures or index futures can be traded.                                                                                                                                                                                              |
| instrument_type | string | Instrument type of a particular contract.                                                                                                                                                                                                                            |

Possible values: , , etc.  
option_type| string| Option type of the option contracts (applicable only for options contract).  
Possible values: ,  
exchange| string| Exchange to which the order is associated.  
Possible values: , , , , , etc.

## JSON files​

These URLs provide access to the complete list of BOD contracts available for trading on Upstox in JSON format.

- [Complete](https://assets.upstox.com/market-quote/instruments/exchange/complete.json.gz)
- [NSE](https://assets.upstox.com/market-quote/instruments/exchange/NSE.json.gz)
- [BSE](https://assets.upstox.com/market-quote/instruments/exchange/BSE.json.gz)
- [MCX](https://assets.upstox.com/market-quote/instruments/exchange/MCX.json.gz)
- [Suspended](https://assets.upstox.com/market-quote/instruments/exchange/suspended-instrument.json.gz)

### Sample JSON Object​

- EQ
- Futures
- Options
- INDEX

Note

- When you're searching for instrument keys within an instrument JSON file, you can employ the and parameters to refine and narrow down the list of instrument keys. For instance, if you're looking for the instrument key for Reliance Equity, specify the as and the as , excluding other segments and instrument types from your search criteria.

### Field Description

| Field Name | Type   | Description                                    |
| ---------- | ------ | ---------------------------------------------- |
| segment    | string | Segment to which the instrument is associated. |

Possible values: , , , , , , , ,  
name| string| The name of the equity.  
exchange| string| Exchange to which the instrument is associated.  
Possible values: , ,  
isin| string| The International Securities Identification Number.  
instrument_type| string| The instrument types for NSE are present at [NSE India](https://www.nseindia.com/market-data/legend-of-series) and for BSE are present at [BSE India](https://www.bseindia.com/markets/equity/EQReports/tra_trading.aspx).  
instrument_key| string| The unique identifier used across Upstox APIs for instrument identification. For the regex pattern applicable to this field, see the [Field Pattern Appendix](/developer/api-documentation/appendix/field-pattern).  
lot_size| number| The size of one lot of the equity.  
freeze_quantity| number| The maximum quantity that can be frozen.  
exchange_token| string| The exchange-specific token for the equity.  
tick_size| number| The minimum price movement of the equity.  
trading_symbol| string| Trading symbol of the instrument.  
short_name| string| A shorter or abbreviated name of the equity.  
security_type| string| Identifies the classification or status of a security within the market. Valid security types can be found in the [Security Type Appendix](/developer/api-documentation/appendix/equity-security-type)

Note

- When you're searching for instrument keys within an instrument JSON file, you can employ the and parameters to refine and narrow down the list of instrument keys. For instance, if you're looking for the instrument key for Reliance Future, specify the as and the as , excluding other segments and instrument types from your search criteria.

### Field Description

| Field Name        | Type    | Description                                                                                                                                                                                                         |
| ----------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| weekly            | boolean | Indicates if the future is weekly.                                                                                                                                                                                  |
| segment           | string  | Segment to which the instrument is associated. Possible values: , , , , , , , ,                                                                                                                                     |
| name              | string  | The name of the future.                                                                                                                                                                                             |
| exchange          | string  | Exchange to which the instrument is associated. Possible values: , ,                                                                                                                                                |
| expiry            | date    | The expiry date of the future.                                                                                                                                                                                      |
| instrument_type   | string  | The type of the future instrument. Possible values:                                                                                                                                                                 |
| underlying_symbol | string  | The symbol of the underlying asset.                                                                                                                                                                                 |
| instrument_key    | string  | The unique identifier used across Upstox APIs for instrument identification. For the regex pattern applicable to this field, see the [Field Pattern Appendix](/developer/api-documentation/appendix/field-pattern). |
| lot_size          | number  | The size of one lot of the future.                                                                                                                                                                                  |
| freeze_quantity   | number  | The maximum quantity that can be frozen.                                                                                                                                                                            |
| exchange_token    | string  | The exchange-specific token for the future.                                                                                                                                                                         |
| minimum_lot       | number  | The minimum lot size for the future.                                                                                                                                                                                |
| underlying_key    | string  | The for the underlying asset.                                                                                                                                                                                       |
| tick_size         | number  | The minimum price movement of the future.                                                                                                                                                                           |
| underlying_type   | string  | The type of the underlying asset. Possible values: , , , ,                                                                                                                                                          |
| trading_symbol    | string  | The symbol used for trading the future. Format:                                                                                                                                                                     |

Note

- When you're searching for instrument keys within an instrument JSON file, you can employ the and parameters to refine and narrow down the list of instrument keys. For instance, if you're looking for the instrument key for Reliance Call Option, specify the as and the as , excluding other segments and instrument types from your search criteria. If you want to search for Put Option then set as .

### Field Description

| Field Name        | Type    | Description                                                                                                                                                                                                         |
| ----------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| weekly            | boolean | Indicates if the option is weekly.                                                                                                                                                                                  |
| segment           | string  | The market segment of the option. Possible values: , , , , , , , ,                                                                                                                                                  |
| name              | string  | The name of the option.                                                                                                                                                                                             |
| exchange          | string  | Exchange to which the instrument is associated. Possible values: , ,                                                                                                                                                |
| expiry            | date    | The expiry date of the option.                                                                                                                                                                                      |
| instrument_type   | string  | The type of the option instrument. Possible values: ,                                                                                                                                                               |
| underlying_symbol | string  | The symbol of the underlying asset.                                                                                                                                                                                 |
| instrument_key    | string  | The unique identifier used across Upstox APIs for instrument identification. For the regex pattern applicable to this field, see the [Field Pattern Appendix](/developer/api-documentation/appendix/field-pattern). |
| strike_price      | number  | The strike price for the option.                                                                                                                                                                                    |
| lot_size          | number  | The size of one lot of the option.                                                                                                                                                                                  |
| freeze_quantity   | number  | The maximum quantity that can be frozen.                                                                                                                                                                            |
| exchange_token    | string  | The exchange-specific token for the option.                                                                                                                                                                         |
| minimum_lot       | number  | The minimum lot size for the option.                                                                                                                                                                                |
| underlying_key    | string  | The for the underlying asset.                                                                                                                                                                                       |
| tick_size         | number  | The minimum price movement of the option.                                                                                                                                                                           |
| underlying_type   | string  | The type of the underlying asset. Possible values: , , , ,                                                                                                                                                          |
| trading_symbol    | string  | The symbol used for trading the option. Format:                                                                                                                                                                     |

Note

- When you're searching for instrument keys within an instrument JSON file, you can employ the and parameters to refine and narrow down the list of instrument keys. For instance, if you're looking for the instrument key for NSE Index, specify the as and the as , excluding other segments and instrument types from your search criteria.

### Field Description​

| Field Name | Type   | Description                                    |
| ---------- | ------ | ---------------------------------------------- |
| segment    | string | Segment to which the instrument is associated. |

Possible values: , , , , , , , ,  
name| string| The name of the index.  
exchange| string| Exchange to which the instrument is associated.  
Possible values: , ,  
instrument_type| string| The type of the option instrument.  
Possible values:  
instrument_key| string| The unique identifier used across Upstox APIs for instrument identification. For the regex pattern applicable to this field, see the [Field Pattern Appendix](/developer/api-documentation/appendix/field-pattern).  
exchange_token| number| The numerical identifier issued by the exchange representing the instrument.  
trading_symbol| string| Trading symbol for the index.

Note

- The files undergo daily refresh at around 6 AM, and they are only refreshed as needed during the day, which is a seldom occurrence.
- The BOD instrument for the next trading day will not include delisted stocks or expired contracts.

[PreviousSelf Generated](/developer/api-documentation/self-generated-sdk)[NextLogin](/developer/api-documentation/login)

- CSV Files
  - Sample CSV Record
  - Field Description
- JSON files
  - Sample JSON Object
  - Field Description

---

## [Field Pattern | Upstox Developer API](https://upstox.com/developer/api-documentation/appendix/field-pattern)

- [](/developer/api-documentation/)
- [Developer API](/developer/api-documentation/open-api)
- [Appendix](/developer/api-documentation/appendix)
- Field Pattern

# Field Pattern

This section outlines the specific regex patterns required for various field inputs, ensuring data consistency and validation. Refer to these specifications to avoid common input errors and streamline data submission processes.

- **order_id**

  - Pattern:

- **symbol**

  - Pattern:

- **financial_year**

  - Pattern:

- **instrumentKey**

  - Pattern:

- **instrument_token**

  - Pattern:

- **instrument_key**

  - Pattern:

- **exchange**

  - Pattern:

[PreviousOrder Status](/developer/api-documentation/appendix/order-status)[NextChangelog](/developer/api-documentation/appendix/change-log)

---

## [Instruments | Upstox Developer API](https://upstox.com/developer/api-documentation/instruments#sample-json-object)

- [](/developer/api-documentation/)
- [Developer API](/developer/api-documentation/open-api)
- Instruments

On this page

# Instruments

Note

- **The CSV format for instruments files is being deprecated.** Switch to the JSON format for improved performance. Details at [CSV Instruments File Deprecation Notice](/developer/api-documentation/announcements/instruments-csv-deprecation-notice).
- The list of suspended instruments is available in the [JSON section](/developer/api-documentation/instruments#json-files) below.

Recommendations

- Use for uniquely identifying instruments, as it remains unique for each instrument. Conversely, may be reused by the exchange for a different instrument after its expiry.
- Use Instruments data in JSON format instead of CSV, as its structure has been designed for enhanced robustness and future scalability, making programmatic processing easier.

## CSV Files​

These URLs provide access to the complete list of BOD contracts available for trading on Upstox in CSV format.

- [Complete](https://assets.upstox.com/market-quote/instruments/exchange/complete.csv.gz)
- [NSE](https://assets.upstox.com/market-quote/instruments/exchange/NSE.csv.gz)
- [BSE](https://assets.upstox.com/market-quote/instruments/exchange/BSE.csv.gz)
- [MCX](https://assets.upstox.com/market-quote/instruments/exchange/MCX.csv.gz)

### Sample CSV Record​

| instrument_key | exchange_token | tradingsymbol | name                | last_price              | expiry | strike     | tick_size | lot_size | instrument_type | option_type | exchange |
| -------------- | -------------- | ------------- | ------------------- | ----------------------- | ------ | ---------- | --------- | -------- | --------------- | ----------- | -------- | ------ |
| NSE_FO         | 164693         | 164693        | RELIANCE24JAN1840CE | RELIANCE INDUSTRIES LTD | 424.8  | 2024-01-25 | 1840.0    | 0.05     | 250             | OPTSTK      | CE       | NSE_FO |

### Field Description​

| Name            | Type   | Description                                                                                                                                                                                                                                                          |
| --------------- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| instrument_key  | string | The unique identifier used across Upstox APIs for instrument identification. For the regex pattern applicable to this field, see the [Field Pattern Appendix](/developer/api-documentation/appendix/field-pattern).                                                  |
| exchange_token  | number | The numerical identifier issued by the exchange representing the instrument.                                                                                                                                                                                         |
| tradingsymbol   | string | Shows the trading symbol which could be a combination of symbol name, instrument, expiry date etc. The format of this value may vary between weekly and monthly contracts, leading to inconsistencies. These inconsistencies have been resolved in the JSON version. |
| name            | string | Name of the company (for equity instruments).                                                                                                                                                                                                                        |
| last_price      | number | Last traded price.                                                                                                                                                                                                                                                   |
| expiry          | string | Expiry date (for derivatives). Data format is                                                                                                                                                                                                                        |
| strike          | number | Indicates the predetermined price at which an option can be bought or sold when it's exercised.                                                                                                                                                                      |
| tick_size       | number | Measure of the minimum upward or downward movement in the price of an instrument.                                                                                                                                                                                    |
| lot_size        | number | Minimum size in which the stock futures or index futures can be traded.                                                                                                                                                                                              |
| instrument_type | string | Instrument type of a particular contract.                                                                                                                                                                                                                            |

Possible values: , , etc.  
option_type| string| Option type of the option contracts (applicable only for options contract).  
Possible values: ,  
exchange| string| Exchange to which the order is associated.  
Possible values: , , , , , etc.

## JSON files​

These URLs provide access to the complete list of BOD contracts available for trading on Upstox in JSON format.

- [Complete](https://assets.upstox.com/market-quote/instruments/exchange/complete.json.gz)
- [NSE](https://assets.upstox.com/market-quote/instruments/exchange/NSE.json.gz)
- [BSE](https://assets.upstox.com/market-quote/instruments/exchange/BSE.json.gz)
- [MCX](https://assets.upstox.com/market-quote/instruments/exchange/MCX.json.gz)
- [Suspended](https://assets.upstox.com/market-quote/instruments/exchange/suspended-instrument.json.gz)

### Sample JSON Object​

- EQ
- Futures
- Options
- INDEX

Note

- When you're searching for instrument keys within an instrument JSON file, you can employ the and parameters to refine and narrow down the list of instrument keys. For instance, if you're looking for the instrument key for Reliance Equity, specify the as and the as , excluding other segments and instrument types from your search criteria.

### Field Description

| Field Name | Type   | Description                                    |
| ---------- | ------ | ---------------------------------------------- |
| segment    | string | Segment to which the instrument is associated. |

Possible values: , , , , , , , ,  
name| string| The name of the equity.  
exchange| string| Exchange to which the instrument is associated.  
Possible values: , ,  
isin| string| The International Securities Identification Number.  
instrument_type| string| The instrument types for NSE are present at [NSE India](https://www.nseindia.com/market-data/legend-of-series) and for BSE are present at [BSE India](https://www.bseindia.com/markets/equity/EQReports/tra_trading.aspx).  
instrument_key| string| The unique identifier used across Upstox APIs for instrument identification. For the regex pattern applicable to this field, see the [Field Pattern Appendix](/developer/api-documentation/appendix/field-pattern).  
lot_size| number| The size of one lot of the equity.  
freeze_quantity| number| The maximum quantity that can be frozen.  
exchange_token| string| The exchange-specific token for the equity.  
tick_size| number| The minimum price movement of the equity.  
trading_symbol| string| Trading symbol of the instrument.  
short_name| string| A shorter or abbreviated name of the equity.  
security_type| string| Identifies the classification or status of a security within the market. Valid security types can be found in the [Security Type Appendix](/developer/api-documentation/appendix/equity-security-type)

Note

- When you're searching for instrument keys within an instrument JSON file, you can employ the and parameters to refine and narrow down the list of instrument keys. For instance, if you're looking for the instrument key for Reliance Future, specify the as and the as , excluding other segments and instrument types from your search criteria.

### Field Description

| Field Name        | Type    | Description                                                                                                                                                                                                         |
| ----------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| weekly            | boolean | Indicates if the future is weekly.                                                                                                                                                                                  |
| segment           | string  | Segment to which the instrument is associated. Possible values: , , , , , , , ,                                                                                                                                     |
| name              | string  | The name of the future.                                                                                                                                                                                             |
| exchange          | string  | Exchange to which the instrument is associated. Possible values: , ,                                                                                                                                                |
| expiry            | date    | The expiry date of the future.                                                                                                                                                                                      |
| instrument_type   | string  | The type of the future instrument. Possible values:                                                                                                                                                                 |
| underlying_symbol | string  | The symbol of the underlying asset.                                                                                                                                                                                 |
| instrument_key    | string  | The unique identifier used across Upstox APIs for instrument identification. For the regex pattern applicable to this field, see the [Field Pattern Appendix](/developer/api-documentation/appendix/field-pattern). |
| lot_size          | number  | The size of one lot of the future.                                                                                                                                                                                  |
| freeze_quantity   | number  | The maximum quantity that can be frozen.                                                                                                                                                                            |
| exchange_token    | string  | The exchange-specific token for the future.                                                                                                                                                                         |
| minimum_lot       | number  | The minimum lot size for the future.                                                                                                                                                                                |
| underlying_key    | string  | The for the underlying asset.                                                                                                                                                                                       |
| tick_size         | number  | The minimum price movement of the future.                                                                                                                                                                           |
| underlying_type   | string  | The type of the underlying asset. Possible values: , , , ,                                                                                                                                                          |
| trading_symbol    | string  | The symbol used for trading the future. Format:                                                                                                                                                                     |

Note

- When you're searching for instrument keys within an instrument JSON file, you can employ the and parameters to refine and narrow down the list of instrument keys. For instance, if you're looking for the instrument key for Reliance Call Option, specify the as and the as , excluding other segments and instrument types from your search criteria. If you want to search for Put Option then set as .

### Field Description

| Field Name        | Type    | Description                                                                                                                                                                                                         |
| ----------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| weekly            | boolean | Indicates if the option is weekly.                                                                                                                                                                                  |
| segment           | string  | The market segment of the option. Possible values: , , , , , , , ,                                                                                                                                                  |
| name              | string  | The name of the option.                                                                                                                                                                                             |
| exchange          | string  | Exchange to which the instrument is associated. Possible values: , ,                                                                                                                                                |
| expiry            | date    | The expiry date of the option.                                                                                                                                                                                      |
| instrument_type   | string  | The type of the option instrument. Possible values: ,                                                                                                                                                               |
| underlying_symbol | string  | The symbol of the underlying asset.                                                                                                                                                                                 |
| instrument_key    | string  | The unique identifier used across Upstox APIs for instrument identification. For the regex pattern applicable to this field, see the [Field Pattern Appendix](/developer/api-documentation/appendix/field-pattern). |
| strike_price      | number  | The strike price for the option.                                                                                                                                                                                    |
| lot_size          | number  | The size of one lot of the option.                                                                                                                                                                                  |
| freeze_quantity   | number  | The maximum quantity that can be frozen.                                                                                                                                                                            |
| exchange_token    | string  | The exchange-specific token for the option.                                                                                                                                                                         |
| minimum_lot       | number  | The minimum lot size for the option.                                                                                                                                                                                |
| underlying_key    | string  | The for the underlying asset.                                                                                                                                                                                       |
| tick_size         | number  | The minimum price movement of the option.                                                                                                                                                                           |
| underlying_type   | string  | The type of the underlying asset. Possible values: , , , ,                                                                                                                                                          |
| trading_symbol    | string  | The symbol used for trading the option. Format:                                                                                                                                                                     |

Note

- When you're searching for instrument keys within an instrument JSON file, you can employ the and parameters to refine and narrow down the list of instrument keys. For instance, if you're looking for the instrument key for NSE Index, specify the as and the as , excluding other segments and instrument types from your search criteria.

### Field Description​

| Field Name | Type   | Description                                    |
| ---------- | ------ | ---------------------------------------------- |
| segment    | string | Segment to which the instrument is associated. |

Possible values: , , , , , , , ,  
name| string| The name of the index.  
exchange| string| Exchange to which the instrument is associated.  
Possible values: , ,  
instrument_type| string| The type of the option instrument.  
Possible values:  
instrument_key| string| The unique identifier used across Upstox APIs for instrument identification. For the regex pattern applicable to this field, see the [Field Pattern Appendix](/developer/api-documentation/appendix/field-pattern).  
exchange_token| number| The numerical identifier issued by the exchange representing the instrument.  
trading_symbol| string| Trading symbol for the index.

Note

- The files undergo daily refresh at around 6 AM, and they are only refreshed as needed during the day, which is a seldom occurrence.
- The BOD instrument for the next trading day will not include delisted stocks or expired contracts.

[PreviousSelf Generated](/developer/api-documentation/self-generated-sdk)[NextLogin](/developer/api-documentation/login)

- CSV Files
  - Sample CSV Record
  - Field Description
- JSON files
  - Sample JSON Object
  - Field Description

---

## [Equity Security Type | Upstox Developer API](https://upstox.com/developer/api-documentation/appendix/equity-security-type)

- [](/developer/api-documentation/)
- [Developer API](/developer/api-documentation/open-api)
- [Appendix](/developer/api-documentation/appendix)
- Equity Security Type

# Equity Security Type

This table presents the list of possible security type an equity can be mapped to.

| Value  | Description                                                                            |
| ------ | -------------------------------------------------------------------------------------- |
| SME    | Equity that caters to small and medium-sized enterprises for market access.            |
| RELIST | Equity that has been reintroduced to trading on the market after a period of absence.  |
| PCA    | Equity subject to regulatory oversight due to financial or operational concerns.       |
| IPO    | Equity initially offered to the public by a company entering the market.               |
| NORMAL | Equity that operates under standard market conditions without special classifications. |

[PreviousPostman Collection](/developer/api-documentation/appendix/postman-collection)[NextExchange](/developer/api-documentation/appendix/exchange)

---

## [Instruments | Upstox Developer API](https://upstox.com/developer/api-documentation/instruments#field-description-1)

- [](/developer/api-documentation/)
- [Developer API](/developer/api-documentation/open-api)
- Instruments

On this page

# Instruments

Note

- **The CSV format for instruments files is being deprecated.** Switch to the JSON format for improved performance. Details at [CSV Instruments File Deprecation Notice](/developer/api-documentation/announcements/instruments-csv-deprecation-notice).
- The list of suspended instruments is available in the [JSON section](/developer/api-documentation/instruments#json-files) below.

Recommendations

- Use for uniquely identifying instruments, as it remains unique for each instrument. Conversely, may be reused by the exchange for a different instrument after its expiry.
- Use Instruments data in JSON format instead of CSV, as its structure has been designed for enhanced robustness and future scalability, making programmatic processing easier.

## CSV Files​

These URLs provide access to the complete list of BOD contracts available for trading on Upstox in CSV format.

- [Complete](https://assets.upstox.com/market-quote/instruments/exchange/complete.csv.gz)
- [NSE](https://assets.upstox.com/market-quote/instruments/exchange/NSE.csv.gz)
- [BSE](https://assets.upstox.com/market-quote/instruments/exchange/BSE.csv.gz)
- [MCX](https://assets.upstox.com/market-quote/instruments/exchange/MCX.csv.gz)

### Sample CSV Record​

| instrument_key | exchange_token | tradingsymbol | name                | last_price              | expiry | strike     | tick_size | lot_size | instrument_type | option_type | exchange |
| -------------- | -------------- | ------------- | ------------------- | ----------------------- | ------ | ---------- | --------- | -------- | --------------- | ----------- | -------- | ------ |
| NSE_FO         | 164693         | 164693        | RELIANCE24JAN1840CE | RELIANCE INDUSTRIES LTD | 424.8  | 2024-01-25 | 1840.0    | 0.05     | 250             | OPTSTK      | CE       | NSE_FO |

### Field Description​

| Name            | Type   | Description                                                                                                                                                                                                                                                          |
| --------------- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| instrument_key  | string | The unique identifier used across Upstox APIs for instrument identification. For the regex pattern applicable to this field, see the [Field Pattern Appendix](/developer/api-documentation/appendix/field-pattern).                                                  |
| exchange_token  | number | The numerical identifier issued by the exchange representing the instrument.                                                                                                                                                                                         |
| tradingsymbol   | string | Shows the trading symbol which could be a combination of symbol name, instrument, expiry date etc. The format of this value may vary between weekly and monthly contracts, leading to inconsistencies. These inconsistencies have been resolved in the JSON version. |
| name            | string | Name of the company (for equity instruments).                                                                                                                                                                                                                        |
| last_price      | number | Last traded price.                                                                                                                                                                                                                                                   |
| expiry          | string | Expiry date (for derivatives). Data format is                                                                                                                                                                                                                        |
| strike          | number | Indicates the predetermined price at which an option can be bought or sold when it's exercised.                                                                                                                                                                      |
| tick_size       | number | Measure of the minimum upward or downward movement in the price of an instrument.                                                                                                                                                                                    |
| lot_size        | number | Minimum size in which the stock futures or index futures can be traded.                                                                                                                                                                                              |
| instrument_type | string | Instrument type of a particular contract.                                                                                                                                                                                                                            |

Possible values: , , etc.  
option_type| string| Option type of the option contracts (applicable only for options contract).  
Possible values: ,  
exchange| string| Exchange to which the order is associated.  
Possible values: , , , , , etc.

## JSON files​

These URLs provide access to the complete list of BOD contracts available for trading on Upstox in JSON format.

- [Complete](https://assets.upstox.com/market-quote/instruments/exchange/complete.json.gz)
- [NSE](https://assets.upstox.com/market-quote/instruments/exchange/NSE.json.gz)
- [BSE](https://assets.upstox.com/market-quote/instruments/exchange/BSE.json.gz)
- [MCX](https://assets.upstox.com/market-quote/instruments/exchange/MCX.json.gz)
- [Suspended](https://assets.upstox.com/market-quote/instruments/exchange/suspended-instrument.json.gz)

### Sample JSON Object​

- EQ
- Futures
- Options
- INDEX

Note

- When you're searching for instrument keys within an instrument JSON file, you can employ the and parameters to refine and narrow down the list of instrument keys. For instance, if you're looking for the instrument key for Reliance Equity, specify the as and the as , excluding other segments and instrument types from your search criteria.

### Field Description

| Field Name | Type   | Description                                    |
| ---------- | ------ | ---------------------------------------------- |
| segment    | string | Segment to which the instrument is associated. |

Possible values: , , , , , , , ,  
name| string| The name of the equity.  
exchange| string| Exchange to which the instrument is associated.  
Possible values: , ,  
isin| string| The International Securities Identification Number.  
instrument_type| string| The instrument types for NSE are present at [NSE India](https://www.nseindia.com/market-data/legend-of-series) and for BSE are present at [BSE India](https://www.bseindia.com/markets/equity/EQReports/tra_trading.aspx).  
instrument_key| string| The unique identifier used across Upstox APIs for instrument identification. For the regex pattern applicable to this field, see the [Field Pattern Appendix](/developer/api-documentation/appendix/field-pattern).  
lot_size| number| The size of one lot of the equity.  
freeze_quantity| number| The maximum quantity that can be frozen.  
exchange_token| string| The exchange-specific token for the equity.  
tick_size| number| The minimum price movement of the equity.  
trading_symbol| string| Trading symbol of the instrument.  
short_name| string| A shorter or abbreviated name of the equity.  
security_type| string| Identifies the classification or status of a security within the market. Valid security types can be found in the [Security Type Appendix](/developer/api-documentation/appendix/equity-security-type)

Note

- When you're searching for instrument keys within an instrument JSON file, you can employ the and parameters to refine and narrow down the list of instrument keys. For instance, if you're looking for the instrument key for Reliance Future, specify the as and the as , excluding other segments and instrument types from your search criteria.

### Field Description

| Field Name        | Type    | Description                                                                                                                                                                                                         |
| ----------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| weekly            | boolean | Indicates if the future is weekly.                                                                                                                                                                                  |
| segment           | string  | Segment to which the instrument is associated. Possible values: , , , , , , , ,                                                                                                                                     |
| name              | string  | The name of the future.                                                                                                                                                                                             |
| exchange          | string  | Exchange to which the instrument is associated. Possible values: , ,                                                                                                                                                |
| expiry            | date    | The expiry date of the future.                                                                                                                                                                                      |
| instrument_type   | string  | The type of the future instrument. Possible values:                                                                                                                                                                 |
| underlying_symbol | string  | The symbol of the underlying asset.                                                                                                                                                                                 |
| instrument_key    | string  | The unique identifier used across Upstox APIs for instrument identification. For the regex pattern applicable to this field, see the [Field Pattern Appendix](/developer/api-documentation/appendix/field-pattern). |
| lot_size          | number  | The size of one lot of the future.                                                                                                                                                                                  |
| freeze_quantity   | number  | The maximum quantity that can be frozen.                                                                                                                                                                            |
| exchange_token    | string  | The exchange-specific token for the future.                                                                                                                                                                         |
| minimum_lot       | number  | The minimum lot size for the future.                                                                                                                                                                                |
| underlying_key    | string  | The for the underlying asset.                                                                                                                                                                                       |
| tick_size         | number  | The minimum price movement of the future.                                                                                                                                                                           |
| underlying_type   | string  | The type of the underlying asset. Possible values: , , , ,                                                                                                                                                          |
| trading_symbol    | string  | The symbol used for trading the future. Format:                                                                                                                                                                     |

Note

- When you're searching for instrument keys within an instrument JSON file, you can employ the and parameters to refine and narrow down the list of instrument keys. For instance, if you're looking for the instrument key for Reliance Call Option, specify the as and the as , excluding other segments and instrument types from your search criteria. If you want to search for Put Option then set as .

### Field Description

| Field Name        | Type    | Description                                                                                                                                                                                                         |
| ----------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| weekly            | boolean | Indicates if the option is weekly.                                                                                                                                                                                  |
| segment           | string  | The market segment of the option. Possible values: , , , , , , , ,                                                                                                                                                  |
| name              | string  | The name of the option.                                                                                                                                                                                             |
| exchange          | string  | Exchange to which the instrument is associated. Possible values: , ,                                                                                                                                                |
| expiry            | date    | The expiry date of the option.                                                                                                                                                                                      |
| instrument_type   | string  | The type of the option instrument. Possible values: ,                                                                                                                                                               |
| underlying_symbol | string  | The symbol of the underlying asset.                                                                                                                                                                                 |
| instrument_key    | string  | The unique identifier used across Upstox APIs for instrument identification. For the regex pattern applicable to this field, see the [Field Pattern Appendix](/developer/api-documentation/appendix/field-pattern). |
| strike_price      | number  | The strike price for the option.                                                                                                                                                                                    |
| lot_size          | number  | The size of one lot of the option.                                                                                                                                                                                  |
| freeze_quantity   | number  | The maximum quantity that can be frozen.                                                                                                                                                                            |
| exchange_token    | string  | The exchange-specific token for the option.                                                                                                                                                                         |
| minimum_lot       | number  | The minimum lot size for the option.                                                                                                                                                                                |
| underlying_key    | string  | The for the underlying asset.                                                                                                                                                                                       |
| tick_size         | number  | The minimum price movement of the option.                                                                                                                                                                           |
| underlying_type   | string  | The type of the underlying asset. Possible values: , , , ,                                                                                                                                                          |
| trading_symbol    | string  | The symbol used for trading the option. Format:                                                                                                                                                                     |

Note

- When you're searching for instrument keys within an instrument JSON file, you can employ the and parameters to refine and narrow down the list of instrument keys. For instance, if you're looking for the instrument key for NSE Index, specify the as and the as , excluding other segments and instrument types from your search criteria.

### Field Description​

| Field Name | Type   | Description                                    |
| ---------- | ------ | ---------------------------------------------- |
| segment    | string | Segment to which the instrument is associated. |

Possible values: , , , , , , , ,  
name| string| The name of the index.  
exchange| string| Exchange to which the instrument is associated.  
Possible values: , ,  
instrument_type| string| The type of the option instrument.  
Possible values:  
instrument_key| string| The unique identifier used across Upstox APIs for instrument identification. For the regex pattern applicable to this field, see the [Field Pattern Appendix](/developer/api-documentation/appendix/field-pattern).  
exchange_token| number| The numerical identifier issued by the exchange representing the instrument.  
trading_symbol| string| Trading symbol for the index.

Note

- The files undergo daily refresh at around 6 AM, and they are only refreshed as needed during the day, which is a seldom occurrence.
- The BOD instrument for the next trading day will not include delisted stocks or expired contracts.

[PreviousSelf Generated](/developer/api-documentation/self-generated-sdk)[NextLogin](/developer/api-documentation/login)

- CSV Files
  - Sample CSV Record
  - Field Description
- JSON files
  - Sample JSON Object
  - Field Description

---

## [Login | Upstox Developer API](https://upstox.com/developer/api-documentation/login#docusaurus_skipToContent_fallback)

- [](/developer/api-documentation/)
- [Developer API](/developer/api-documentation/open-api)
- Login

# Login

## [description AuthorizeLogin flow for the API users.](/developer/api-documentation/authorize)## [description Get TokenGet access token for the API user after login.](/developer/api-documentation/get-token)## [description LogoutLogout flow for the API users.](/developer/api-documentation/logout)

NOTE

You also have the option to select [TOTP (Time-based One-Time Password)](https://en.wikipedia.org/wiki/Time-based_one-time_password) as a more secure method for 2FA, compared to the usual SMS OTP, for a safer login. Learn more about activating TOTP on your Upstox account [here](https://help.upstox.com/support/solutions/articles/260346-what-is-totp-and-how-to-enable-totp-for-my-account-from-upstox-web-platform-).

[PreviousInstruments](/developer/api-documentation/instruments)[NextAuthorize](/developer/api-documentation/authorize)

---

## [Get Token | Upstox Developer API](https://upstox.com/developer/api-documentation/get-token)

- [](/developer/api-documentation/)
- [Developer API](/developer/api-documentation/open-api)
- [Login](/developer/api-documentation/login)
- Get Token

## Get Token​

API to acquire an access token via an authorization_code exchange and concurrently includes the user's profile in the response.

NOTE

The obtained through this API has a specific validity period that lasts until the following day, regardless of the time it was generated. For instance, if you generate a token at 8 PM on Tuesday, it will expire at 3:30 AM on Wednesday. This also means that a token created at 2:30 AM on Wednesday will still expire at 3:30 AM on the same Wednesday. Therefore, users are advised to plan their activities accordingly, ensuring they accommodate the token's expiration schedule in their usage.

### Header Parameters​

| Name         | Required | Type   | Description                                                             |
| ------------ | -------- | ------ | ----------------------------------------------------------------------- |
| Content-Type | true     | string | Indicates the media type of the resource, set as .                      |
| Accept       | true     | string | Defines the content format the client expects, which should be set to . |

### Request Body​

| Name          | Required | Type   | Description                                                                                                                                                   |
| ------------- | -------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| code          | true     | string | The is a unique parameter included in the URL upon a successful [Authorize API](/developer/api-documentation/authorize) authentication.                       |
| client_id     | true     | string | The API key obtained during the app generation process.                                                                                                       |
| client_secret | true     | string | The API secret obtained during the app generation process. This private key remains confidential, known only to the application and the authorization server. |
| redirect_uri  | true     | string | The URL provided during app generation.                                                                                                                       |
| grant_type    | true     | string | This value must always be .                                                                                                                                   |

NOTE

The sent as part of this request is valid for a single use, regardless of whether the access token generation succeeds or encounters an issue.

**Responses**

- 200
- 4XX

---

### Response Body​

| Name      | Type     | Description                                                                                                                                     |
| --------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| email     | string   | E-mail address of the user                                                                                                                      |
| exchanges | string[] | List of exchanges enabled for the user. Valid exchanges can be found in the [Exchange Appendix](/developer/api-documentation/appendix/exchange) |
| products  | string[] | Lists the types of products enabled for the user.                                                                                               |

Possible values: , , ,  
broker| string| The broker ID  
user_id| string| Uniquely identifies the user (commonly referred as UCC)  
user_name| string| Name of the user  
order_types| string[]| Order types enabled for the user.  
Possible values: , , ,  
user_type| string| Identifies the user's registered role with the broker. This will be individual for all retail users  
poa| boolean| Indicates whether the user has authorized power of attorney for transactions.  
is_active| boolean| Indicates if the account status is active.  
access_token| string| The authentication token to be used with every subsequent API request.  
extended_token| string| This token is designed for prolonged usage, primarily for read-only access to various API endpoints. For more detailed information on the extended token, including its benefits and how to opt for it, please refer to the [Extended Token Documentation](/developer/api-documentation/authentication#extended-token).

NOTE

If a user attempting to log in has no active segments, the error will occur, preventing the Token API from generating the access_token. To resolve this, users must manually reactivate their segment through the Upstox web or mobile application before attempting to log in again.

### Error codes​

| Error code  | Description                                                                                                                                            |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| UDAPI100069 | **Check your 'client_id' and 'client_secret'; one or both are incorrect.** \- Thrown when one of the credentials you've passed to this API is invalid. |
| UDAPI100070 | **The 'redirect_uri' provided is invalid. Please enter the valid URI and try again.** \- Thrown when the passed to this API is invalid.                |
| UDAPI100057 | **Invalid Auth code** \- Thrown when the value passed to the API is invalid.                                                                           |

## Examples​

A comprehensive set of examples is provided to illustrate various use cases and implementation scenarios for this API. To view detailed examples and access sample code, please refer to: [API Examples](/developer/api-documentation/example-code/login/get-token).

Loading...

[PreviousAuthorize](/developer/api-documentation/authorize)[NextLogout](/developer/api-documentation/logout)

---

## [Logout | Upstox Developer API](https://upstox.com/developer/api-documentation/logout)

- [](/developer/api-documentation/)
- [Developer API](/developer/api-documentation/open-api)
- [Login](/developer/api-documentation/login)
- Logout

## Logout​

API to log out a user's active session, making the current session no longer valid. After logging out, the user will need to log in again for any further interactions.

### Header Parameters​

| Name          | Required | Type   | Description                                                                                         |
| ------------- | -------- | ------ | --------------------------------------------------------------------------------------------------- |
| Authorization | true     | string | Requires the format where is obtained from the [Token API](/developer/api-documentation/get-token). |
| Accept        | true     | string | Defines the content format the client expects, which should be set to .                             |

**Responses**

- 200

---

### Response Body​

| Name   | Type    | Description                                                                          |
| ------ | ------- | ------------------------------------------------------------------------------------ |
| status | string  | A string indicating the outcome of the request. Typically for successful operations. |
| data   | boolean | Indicates whether the logout was successful                                          |

## Examples​

A comprehensive set of examples is provided to illustrate various use cases and implementation scenarios for this API. To view detailed examples and access sample code, please refer to: [API Examples](/developer/api-documentation/example-code/login/logout).

Loading...

[PreviousGet Token](/developer/api-documentation/get-token)[NextUser](/developer/api-documentation/user)

---

## [User | Upstox Developer API](https://upstox.com/developer/api-documentation/user#docusaurus_skipToContent_fallback)

- [](/developer/api-documentation/)
- [Developer API](/developer/api-documentation/open-api)
- User

# User

## [description Get ProfileGet user profile related information.](/developer/api-documentation/get-profile)## [description Get Fund And MarginGet user fund related information in equity and commodity market.](/developer/api-documentation/get-user-fund-margin)

[PreviousLogout](/developer/api-documentation/logout)[NextGet Profile](/developer/api-documentation/get-profile)

---

## [Get Profile | Upstox Developer API](https://upstox.com/developer/api-documentation/get-profile)

- [](/developer/api-documentation/)
- [Developer API](/developer/api-documentation/open-api)
- [User](/developer/api-documentation/user)
- Get Profile

## Get Profile​

API to retrieve user profile data, which encompasses details such as supported exchanges, enabled product offerings, and permitted order types. If you're business and developing an application for multi-client API usage, you can utilize this data to display in the user's profile section.

### Header Parameters​

| Name          | Required | Type   | Description                                                                                         |
| ------------- | -------- | ------ | --------------------------------------------------------------------------------------------------- |
| Authorization | true     | string | Requires the format where is obtained from the [Token API](/developer/api-documentation/get-token). |
| Accept        | true     | string | Defines the content format the client expects, which should be set to .                             |

**Responses**

- 200
- 4XX

---

### Response Body​

| Name           | Type     | Description                                                                                                                                     |
| -------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| status         | string   | A string indicating the outcome of the request. Typically for successful operations.                                                            |
| data           | object   | Response data for user profile                                                                                                                  |
| data.email     | string   | E-mail address of the user                                                                                                                      |
| data.exchanges | string[] | List of exchanges enabled for the user. Valid exchanges can be found in the [Exchange Appendix](/developer/api-documentation/appendix/exchange) |
| data.products  | string[] | Lists the types of products enabled for the user.                                                                                               |

Possible values: , , ,  
data.broker| string| The broker ID  
data.user_id| string| Uniquely identifies the user (commonly referred as UCC)  
data.user_name| string| Name of the user  
data.order_types| string[]| Order types enabled for the user.  
Possible values: , , ,  
data.user_type| string| Identifies the user's registered role at the broker. This will be individual for all retail users  
data.poa| boolean| Indicates whether the user has authorized power of attorney for transactions.  
data.is_active| boolean| Indicates if the account status is active.

### Error codes​

| Error code  | Description                                                                                                                                                                                                                                                               |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| UDAPI100058 | **No segments for these users are active. Manual reactivation is recommended from Upstox app/web.** \- Thrown when the signing-in user lacks active segments on their account. It's recommended that the user re-enable these segments through the Upstox app or website. |

## Examples​

A comprehensive set of examples is provided to illustrate various use cases and implementation scenarios for this API. To view detailed examples and access sample code, please refer to: [API Examples](/developer/api-documentation/example-code/user/get-profie).

Loading...

[PreviousUser](/developer/api-documentation/user)[NextGet Fund And Margin](/developer/api-documentation/get-user-fund-margin)

---

## [Get Fund And Margin | Upstox Developer API](https://upstox.com/developer/api-documentation/get-user-fund-margin)

- [](/developer/api-documentation/)
- [Developer API](/developer/api-documentation/open-api)
- [User](/developer/api-documentation/user)
- Get Fund And Margin

## Get Fund And Margin​

API to retrieve user funds data for both the equity and commodity markets, including data such as the margin utilized by the user, the available margin for trading, and the total payin amount during the day.

### Header Parameters​

| Name          | Required | Type   | Description                                                                                         |
| ------------- | -------- | ------ | --------------------------------------------------------------------------------------------------- |
| Authorization | true     | string | Requires the format where is obtained from the [Token API](/developer/api-documentation/get-token). |
| Accept        | true     | string | Defines the content format the client expects, which should be set to .                             |

### Query Parameters​

| Name    | Required | Type   | Description                                                                                                                                                                  |
| ------- | -------- | ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| segment | false    | string | Determines the market segment related to the transaction. Without a specified segment in the request, the response will encompass results for both commodities and equities. |

Possible values: for Equity use , for Commodity use

**Responses**

- 200
- 4XX

---

### Response Body​

| Name                  | Type   | Description                                                                                                                 |
| --------------------- | ------ | --------------------------------------------------------------------------------------------------------------------------- |
| status                | string | A string indicating the outcome of the request. Typically for successful operations.                                        |
| data                  | object | Response data for Balance                                                                                                   |
| data.used_margin      | float  | Positive values denote the amount blocked into an Open order or position. Negative value denotes the amount being released. |
| data.payin_amount     | float  | Instant payin will reflect here                                                                                             |
| data.span_margin      | float  | Amount blocked on futures and options towards SPAN                                                                          |
| data.adhoc_margin     | float  | Payin amount credited through a manual process                                                                              |
| data.notional_cash    | float  | The amount maintained for withdrawal                                                                                        |
| data.available_margin | float  | Total margin available for trading                                                                                          |
| data.exposure_margin  | float  | Amount blocked on futures and options towards Exposure                                                                      |

### Error codes​

| Error code  | Description                                                                                                                                               |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| UDAPI100072 | **The Funds service is accessible from 5:30 AM to 12:00 AM IST daily** \- Thrown when an funds API is called between midnight and 5:30 AM in the morning. |

NOTE

- The Funds service is down for maintenance from 12:00 AM to 5:30 AM IST daily and is not available for usage during these hours. Users are advised to plan their activities accordingly.

## Examples​

A comprehensive set of examples is provided to illustrate various use cases and implementation scenarios for this API. To view detailed examples and access sample code, please refer to: [API Examples](/developer/api-documentation/example-code/user/get-fund-and-margin).

Loading...

[PreviousGet Profile](/developer/api-documentation/get-profile)[NextCharges](/developer/api-documentation/charges)

---

## [Charges | Upstox Developer API](https://upstox.com/developer/api-documentation/charges#docusaurus_skipToContent_fallback)

- [](/developer/api-documentation/)
- [Developer API](/developer/api-documentation/open-api)
- Charges

# Charges

## [description Brokerage DetailsCalculate brokerage charges for an order.](/developer/api-documentation/get-brokerage)

[PreviousGet Fund And Margin](/developer/api-documentation/get-user-fund-margin)[NextBrokerage Details](/developer/api-documentation/get-brokerage)

---

## [Brokerage Details | Upstox Developer API](https://upstox.com/developer/api-documentation/get-brokerage)

- [](/developer/api-documentation/)
- [Developer API](/developer/api-documentation/open-api)
- [Charges](/developer/api-documentation/charges)
- Brokerage Details

## Brokerage Details​

API for calculating brokerage fees associated with stock. It accepts input parameters like the instrument, quantity, and other necessary details, and provides a comprehensive breakdown of the total charges.

### Header Parameters​

| Name          | Required | Type   | Description                                                                                         |
| ------------- | -------- | ------ | --------------------------------------------------------------------------------------------------- |
| Authorization | true     | string | Requires the format where is obtained from the [Token API](/developer/api-documentation/get-token). |
| Accept        | true     | string | Defines the content format the client expects, which should be set to .                             |

### Query Parameters​

| Name             | Required | Type            | Description                                                                                                                                                   |
| ---------------- | -------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| instrument_token | true     | string          | Key of the instrument. For the regex pattern applicable to this field, see the [Field Pattern Appendix](/developer/api-documentation/appendix/field-pattern). |
| quantity         | true     | integer (int32) | Quantity with which the order is to be placed                                                                                                                 |
| product          | true     | string          | Product with which the order is to be placed                                                                                                                  |
| transaction_type | true     | string          | Indicates whether its a BUY or SELL order                                                                                                                     |
| price            | true     | number (float)  | Price with which the order is to be placed                                                                                                                    |

**Responses**

- 200
- 4XX

---

### Response Body​

| Name                                     | Type   | Description                                                                                                                        |
| ---------------------------------------- | ------ | ---------------------------------------------------------------------------------------------------------------------------------- |
| status                                   | string | A string indicating the outcome of the request. Typically for successful operations.                                               |
| data                                     | object | Response data for brokerage                                                                                                        |
| data.charges                             | object | Response data for charges details                                                                                                  |
| data.charges.total                       | float  | Total charges for the order                                                                                                        |
| data.charges.brokerage                   | float  | Brokerage charges for the order                                                                                                    |
| data.charges.taxes                       | object | Taxes levied on order                                                                                                              |
| data.charges.taxes.gst                   | float  | GST charges                                                                                                                        |
| data.charges.taxes.stt                   | float  | STT charges                                                                                                                        |
| data.charges.taxes.stamp_duty            | float  | Stamp duty charges                                                                                                                 |
| data.charges.other_charges               | object | Other applicable charges                                                                                                           |
| data.charges.other_charges.transaction   | float  | Transaction charges                                                                                                                |
| data.charges.other_charges.clearing      | float  | Clearing charges                                                                                                                   |
| data.charges.other_charges.ipft          | float  | IPF charges                                                                                                                        |
| data.charges.other_charges.sebi_turnover | float  | SEBI turnover charges                                                                                                              |
| data.charges.dp_plan                     | object | dpPlan detail                                                                                                                      |
| data.charges.dp_plan.name                | string | Name of the user's Depository Participant plan, indicating the specific DP service they are enrolled in.                           |
| data.charges.dp_plan.min_expense         | float  | Daily minimum charges per scrip on sales, not included in brokerage calculations, indicating extra costs under the user's DP plan. |

Notice of Deprecation

The camelCase fields (, and ) are deprecated and will be removed in future versions. Use the snake_case versions for consistency.

### Error codes​

| Error code | Description                                                                     |
| ---------- | ------------------------------------------------------------------------------- |
| UDAPI1059  | **The instrument_token is of invalid format** \- The given format isn't correct |
| UDAPI1060  | **The quantity is required** \- The field needs to be provided                  |
| UDAPI1064  | **The quantity cannot be zero** \- You cannot provide zero as the value         |
| UDAPI1063  | **The product is required** \- The field is missing                             |
| UDAPI1054  | **The 'product' is invalid** \- The provided value for is not acceptable        |
| UDAPI1062  | **The transaction_type is required** \- You need to provide the field           |
| UDAPI1057  | **The ''transaction_type'' is invalid** \- The given value for is not valid     |
| UDAPI1061  | **The price is required** \- The field is missing                               |
| UDAPI1065  | **The price cannot be zero** \- Zero is not an acceptable value for             |

## Examples​

A comprehensive set of examples is provided to illustrate various use cases and implementation scenarios for this API. To view detailed examples and access sample code, please refer to: [API Examples](/developer/api-documentation/example-code/charges/brokerage-details).

Loading...

[PreviousCharges](/developer/api-documentation/charges)[NextOrders](/developer/api-documentation/orders)

---

## [Orders | Upstox Developer API](https://upstox.com/developer/api-documentation/orders#docusaurus_skipToContent_fallback)

- [](/developer/api-documentation/)
- [Developer API](/developer/api-documentation/open-api)
- Orders

# Orders

NOTE

- If you represent a business aiming to incorporate order flow management (including placing, canceling, and modifying orders), please visit the [Uplink Business](/developer/api-documentation/uplink-business/introduction). The direct HTTP order placement API integration is intended for individual API users.

Important

- In adherence to CDSL regulations, customers without a DDPI/POA are obligated to use a combination of the CDSL TPIN and OTP to provide the necessary authorization for the deduction of securities from their demat account when engaging in delivery sale transactions.

## [description Place OrderPlace an order with all possible combinations.](/developer/api-documentation/place-order)## [description Modify OrderModify pending or open orders.](/developer/api-documentation/modify-order)## [description Cancel OrderCancel pending or open orders.](/developer/api-documentation/cancel-order)## [description Get Order DetailsGet the latest status and details for an order.](/developer/api-documentation/get-order-details)## [description Get Order HistoryGet order history for an order.](/developer/api-documentation/get-order-history)## [description Get Order BookGet the list of all orders placed during the day.](/developer/api-documentation/get-order-book)## [description Get TradesGet the list of all trades for the day.](/developer/api-documentation/get-trade-history)## [description Get Order TradesGet the list of trades executed for an order.](/developer/api-documentation/get-trades-by-order)## [description Get Trade HistoryGet the list of historical trades](/developer/api-documentation/get-historical-trades)

[PreviousBrokerage Details](/developer/api-documentation/get-brokerage)[NextPlace Order](/developer/api-documentation/place-order)

---

## [Place Order | Upstox Developer API](https://upstox.com/developer/api-documentation/place-order)

- [](/developer/api-documentation/)
- [Developer API](/developer/api-documentation/open-api)
- [Orders](/developer/api-documentation/orders)
- Place Order

## Place Order​

API to place an order to the exchange. The instrument_token required for the stock or contracts should be obtained from the [BOD instruments](/developer/api-documentation/instruments).

Upon successfully placing the order with the exchange, a unique order_id is provided in the success response, which can be utilized for order modification or cancellation. If you intend to place an order outside of market hours, the 'is_amo' (After Market Order) should be set to 'true'. You can assign a tag(unique identifier) to your order, allowing you to retrieve orders associated with that tag using the [Order History API](/developer/api-documentation/get-order-history).

NOTE

If you represent a business aiming to incorporate order flow management (including placing, canceling, and modifying orders), please visit the [Uplink Business](/developer/api-documentation/uplink-business/introduction). The direct HTTP order placement API integration is intended for individual API users.

Important

- Currently product type is not allowed.
- In adherence to CDSL regulations, customers without a DDPI/POA are obligated to use a combination of the CDSL TPIN and OTP to provide the necessary authorization for the deduction of securities from their demat account when engaging in delivery sale transactions.

### Header Parameters​

| Name          | Required | Type   | Description                                                                                         |
| ------------- | -------- | ------ | --------------------------------------------------------------------------------------------------- |
| Authorization | true     | string | Requires the format where is obtained from the [Token API](/developer/api-documentation/get-token). |
| Content-Type  | true     | string | Indicates the media type of the resource, set as .                                                  |
| Accept        | true     | string | Defines the content format the client expects, which should be set to .                             |

### Request Body​

| Name     | Required | Type            | Description                                    |
| -------- | -------- | --------------- | ---------------------------------------------- |
| quantity | true     | integer (int32) | Quantity with which the order is to be placed. |

For commodity - number of lots is accepted.  
For other Futures & Options and equities - number of units is accepted in multiples of the tick size.  
product| true| string| Signifies if the order was either Intraday or Delivery.  
Possible values: , .  
validity| true| string| It can be one of the following - DAY(default), IOC.  
Possible values: , .  
price| true| number (float)| Price at which the order will be placed  
tag| false| string| Tag for a particular order  
instrument_token| true| string| Key of the instrument. For the regex pattern applicable to this field, see the [Field Pattern Appendix](/developer/api-documentation/appendix/field-pattern).  
order_type| true| string| Type of order. It can be one of the following MARKET refers to market order LIMIT refers to Limit Order SL refers to Stop Loss Limit SL-M refers to Stop Loss Market.  
Possible values: , , , .  
transaction_type| true| string| Indicates whether its a buy or sell order.  
Possible values: , .  
disclosed_quantity| true| integer (int32)| The quantity that should be disclosed in the market depth  
trigger_price| true| number (float)| If the order is a stop loss order then the trigger price to be set is mentioned here  
is_amo| true| boolean| Signifies if the order is an After Market Order

**Responses**

- 200
- 4XX

---

### Response Body​

| Name          | Type   | Description                                                                          |
| ------------- | ------ | ------------------------------------------------------------------------------------ |
| status        | string | A string indicating the outcome of the request. Typically for successful operations. |
| data          | object | Response data for place order request                                                |
| data.order_id | string | An order ID for the order request placed                                             |

### Error codes​

| Error code  | Description                                                                                                                                                                |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| UDAPI1026   | **Instrument key is required** \- You need to provide the instrument key for this operation.                                                                               |
| UDAPI1004   | **Valid order type is required** \- Please ensure to provide a recognized order type.                                                                                      |
| UDAPI1056   | **The 'order_type' is invalid** \- The specified order type isn't acceptable.                                                                                              |
| UDAPI1057   | **The 'transaction_type' is invalid** \- The given transaction type is not valid.                                                                                          |
| UDAPI1006   | **Product is required** \- You must specify the product in your request.                                                                                                   |
| UDAPI1054   | **The 'product' is invalid** \- The provided product value doesn't match any accepted values.                                                                              |
| UDAPI1007   | **Validity is required** \- You need to provide the duration the order will remain in effect.                                                                              |
| UDAPI1055   | **The 'validity' is invalid** \- The specified order validity isn't recognized.                                                                                            |
| UDAPI1008   | **Price is required** \- Please specify the price in your request.                                                                                                         |
| UDAPI100049 | **Access to this API has been restricted for your account. Please use 'Uplink Business' to place/modify/cancel the order.** \- Use 'Uplink Business' for order operations. |
| UDAPI1052   | **The order 'quantity' cannot be zero** \- You cannot set the order quantity to zero.                                                                                      |
| UDAPI1040   | **Price not required** \- You shouldn't specify a price for this type of order.                                                                                            |
| UDAPI1043   | **The 'price' is required** \- A valid price value needs to be provided for this order type.                                                                               |
| UDAPI1041   | **The 'price' and 'trigger_price' both are required** \- Ensure to specify both price values in your request.                                                              |
| UDAPI1042   | **Only 'trigger_price' is required** \- Only the trigger price needs to be provided, not the regular price.                                                                |
| UDAPI1037   | **Trigger price should be less than limit price** \- Ensure your trigger price is set below the limit price.                                                               |
| UDAPI1038   | **Trigger price should be greater than limit price** \- The trigger price should exceed the limit price value.                                                             |
| UDAPI100011 | **Invalid Instrument key** \- The instrument key you provided doesn't match any recognized keys.                                                                           |
| UDAPI100039 | **AMO orders cannot be placed during the market hours** \- After Market Order (AMO) is not valid during active market sessions.                                            |

## Examples​

A comprehensive set of examples is provided to illustrate various use cases and implementation scenarios for this API. To view detailed examples and access sample code, please refer to: [API Examples](/developer/api-documentation/example-code/orders/place-order).

Loading...

[PreviousOrders](/developer/api-documentation/orders)[NextModify Order](/developer/api-documentation/modify-order)

---

## [Modify Order | Upstox Developer API](https://upstox.com/developer/api-documentation/modify-order)

- [](/developer/api-documentation/)
- [Developer API](/developer/api-documentation/open-api)
- [Orders](/developer/api-documentation/orders)
- Modify Order

## Modify Order​

API to modify an open or pending order.To perform a modification, the orderId is a required field. Along with the orderId, you should include any optional parameters that require modification. If no optional parameters are included in the modification request, the default values will be assumed from the original order.

### Header Parameters​

| Name          | Required | Type   | Description                                                                                         |
| ------------- | -------- | ------ | --------------------------------------------------------------------------------------------------- |
| Authorization | true     | string | Requires the format where is obtained from the [Token API](/developer/api-documentation/get-token). |
| Content-Type  | true     | string | Indicates the media type of the resource, set as .                                                  |
| Accept        | true     | string | Defines the content format the client expects, which should be set to .                             |

### Request Body​

| Name     | Required | Type            | Description                                                         |
| -------- | -------- | --------------- | ------------------------------------------------------------------- |
| quantity | false    | integer (int32) | Quantity with which the order was placed                            |
| validity | true     | string          | Order validity (DAY- Day and IOC- Immediate or Cancel (IOC) order). |

Possible values: , .  
price| true| number (float)| Price at which the order was placed  
order_id| true| string| The order ID for which the order must be modified. For the regex pattern applicable to this field, see the [Field Pattern Appendix](/developer/api-documentation/appendix/field-pattern).  
order_type| true| string| Type of order. It can be one of the following  
MARKET refers to market order  
LIMILT refers to Limit Order  
SL refers to Stop Loss Limit  
SL-M refers to Stop Loss Market.  
Possible values: , , , .  
disclosed_quantity| false| integer (int32)| Indicates the volume to be displayed in the market depth. If provided, this value must be non-zero.  
trigger_price| true| number (float)| If the order is a stop loss order then the trigger price to be set is mentioned here

**Responses**

- 200
- 4XX

---

### Response Body​

| Name          | Type   | Description                                                                          |
| ------------- | ------ | ------------------------------------------------------------------------------------ |
| status        | string | A string indicating the outcome of the request. Typically for successful operations. |
| data          | object | Response data for modify order request                                               |
| data.order_id | string | Order ID                                                                             |

### Error codes​

| Error code  | Description                                                                                                                                                                |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| UDAPI1004   | **Valid order type is required** \- Please ensure you provide an acceptable type for the order.                                                                            |
| UDAPI1007   | **Validity is required** \- You need to specify the duration or validity for the order.                                                                                    |
| UDAPI1056   | **The 'order_type' is invalid** \- The order type you've provided isn't recognized or accepted.                                                                            |
| UDAPI1055   | **The 'validity' is invalid** \- The provided validity doesn't match any of the recognized types.                                                                          |
| UDAPI1008   | **Price is required** \- Please specify the desired price for your order.                                                                                                  |
| UDAPI1036   | **The 'trigger_price' is required** \- A trigger price must be specified for this type of order.                                                                           |
| UDAPI1030   | **'price' is not required** \- For this order type, you don't need to specify a price.                                                                                     |
| UDAPI1029   | **'price' is required** \- A valid price must be provided for this type of order.                                                                                          |
| UDAPI1031   | **Price and Trigger price both are required** \- Both price values, regular and trigger, need to be provided for this order.                                               |
| UDAPI1032   | **Only 'trigger_price' is required** \- For this type of order, only a trigger price value needs to be specified.                                                          |
| UDAPI100049 | **Access to this API has been restricted for your account. Please use 'Uplink Business' to place/modify/cancel the order.** \- Use 'Uplink Business' for order operations. |
| UDAPI100010 | **Order not found** \- The system couldn't locate the order you're referring to.                                                                                           |
| UDAPI100041 | **Modifications of already cancelled/rejected/completed orders is not allowed** \- You cannot make changes to orders that are already finalized in some manner.            |
| UDAPI1039   | **Disclosed quantity should not be less than 10% of the quantity** \- The revealed amount in your order should be at least 10% of the total order amount.                  |
| UDAPI1003   | **Order id is required** \- Thrown when order number is not provided.                                                                                                      |

## Examples​

A comprehensive set of examples is provided to illustrate various use cases and implementation scenarios for this API. To view detailed examples and access sample code, please refer to: [API Examples](/developer/api-documentation/example-code/orders/modify-order).

Loading...

[PreviousPlace Order](/developer/api-documentation/place-order)[NextCancel Order](/developer/api-documentation/cancel-order)

---

## [Cancel Order | Upstox Developer API](https://upstox.com/developer/api-documentation/cancel-order)

- [](/developer/api-documentation/)
- [Developer API](/developer/api-documentation/open-api)
- [Orders](/developer/api-documentation/orders)
- Cancel Order

## Cancel Order​

API to cancel an open or pending which can be applied to both After Market Orders (AMO) and regular orders. It may also serve to exit a Cover Order (CO).

### Header Parameters​

| Name          | Required | Type   | Description                                                                                         |
| ------------- | -------- | ------ | --------------------------------------------------------------------------------------------------- |
| Authorization | true     | string | Requires the format where is obtained from the [Token API](/developer/api-documentation/get-token). |
| Accept        | true     | string | Defines the content format the client expects, which should be set to .                             |

### Query Parameters​

| Name     | Required | Type   | Description                                                                                                                                                                                |
| -------- | -------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| order_id | true     | string | The order ID for which the order must be cancelled. For the regex pattern applicable to this field, see the [Field Pattern Appendix](/developer/api-documentation/appendix/field-pattern). |

**Responses**

- 200
- 4XX

---

### Response Body​

| Name          | Type   | Description                                                                          |
| ------------- | ------ | ------------------------------------------------------------------------------------ |
| status        | string | A string indicating the outcome of the request. Typically for successful operations. |
| data          | object | Response data for Cancel order request                                               |
| data.order_id | string | Reference order ID                                                                   |

### Error codes​

| Error code  | Description                                                                                                                                                                |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| UDAPI1023   | **Order id is required** \- Please ensure you provide an order id.                                                                                                         |
| UDAPI1010   | **Order id accepts only alphanumeric characters and '-'.** \- The order id you've provided isn't accepted.                                                                 |
| UDAPI100049 | **Access to this API has been restricted for your account. Please use 'Uplink Business' to place/modify/cancel the order.** \- Use 'Uplink Business' for order operations. |
| UDAPI100010 | **Order not found** \- The system couldn't locate the order you're referring to.                                                                                           |
| UDAPI100040 | **Cancel of already cancelled/rejected/completed order is not allowed** \- You cannot cancel orders that are already finalized in some manner.                             |

## Examples​

A comprehensive set of examples is provided to illustrate various use cases and implementation scenarios for this API. To view detailed examples and access sample code, please refer to: [API Examples](/developer/api-documentation/example-code/orders/cancel-order).

Loading...

[PreviousModify Order](/developer/api-documentation/modify-order)[NextGet Order Details](/developer/api-documentation/get-order-details)

---

## [Get Trades | Upstox Developer API](https://upstox.com/developer/api-documentation/get-trade-history)

- [](/developer/api-documentation/)
- [Developer API](/developer/api-documentation/open-api)
- [Orders](/developer/api-documentation/orders)
- Get Trades

## Get Trades​

API to retrieve the list of all trades executed for the day. An order, initially submitted as one entity, can be executed in smaller segments based on market situation. Each of these partial executions constitutes a trade, and a single order may consist of several such trades.

### Header Parameters​

| Name          | Required | Type   | Description                                                                                         |
| ------------- | -------- | ------ | --------------------------------------------------------------------------------------------------- |
| Authorization | true     | string | Requires the format where is obtained from the [Token API](/developer/api-documentation/get-token). |
| Accept        | true     | string | Defines the content format the client expects, which should be set to .                             |

**Responses**

- 200

---

### Response Body​

| Name            | Type     | Description                                                                                                                                        |
| --------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| status          | string   | A string indicating the outcome of the request. Typically for successful operations.                                                               |
| data            | object[] | Response data for trades                                                                                                                           |
| data[].exchange | string   | Exchange to which the order is associated. Valid exchanges can be found in the [Exchange Appendix](/developer/api-documentation/appendix/exchange) |
| data[].product  | string   | Signifies if the order was either Intraday, Delivery or CO.                                                                                        |

Possible values: , , , .  
data[].trading_symbol| string| Shows the trading symbol which could be a combination of symbol name, instrument, expiry date etc  
data[].instrument_token| string| Key of the instrument. For the regex pattern applicable to this field, see the [Field Pattern Appendix](/developer/api-documentation/appendix/field-pattern).  
data[].order_type| string| Type of order. It can be one of the following MARKET refers to market order LIMIT refers to Limit Order SL refers to Stop Loss Limit SL-M refers to Stop Loss Market.  
Possible values: , , , .  
data[].transaction_type| string| Indicates whether its a buy or sell order.  
Possible values: , .  
data[].quantity| int32| The total quantity traded from this particular order  
data[].exchange_order_id| string| Unique order ID assigned by the exchange for the order placed  
data[].order_id| string| Unique order ID assigned internally for the order placed  
data[].exchange_timestamp| string| User readable time at when the trade occurred  
data[].average_price| float| Price at which the traded quantity is traded  
data[].trade_id| string| Trade ID generated from exchange towards traded transaction  
data[].order_ref_id| string| Uniquely identifies an order for internal usage.  
data[].order_timestamp| string| User readable timestamp at which the order was placed

Notice of Deprecation

The lowercase field () is deprecated and will be removed in future versions. Use the snake_case versions for consistency.

## Examples​

A comprehensive set of examples is provided to illustrate various use cases and implementation scenarios for this API. To view detailed examples and access sample code, please refer to: [API Examples](/developer/api-documentation/example-code/orders/get-trades).

Loading...

[PreviousGet Order Book](/developer/api-documentation/get-order-book)[NextGet Order Trades](/developer/api-documentation/get-trades-by-order)

---

## [Get Order Trades | Upstox Developer API](https://upstox.com/developer/api-documentation/get-trades-by-order)

- [](/developer/api-documentation/)
- [Developer API](/developer/api-documentation/open-api)
- [Orders](/developer/api-documentation/orders)
- Get Order Trades

## Get Order Trades​

API to retrieve the list of all trades executed for a specific order.To access the trade information, you need to pass order_id.

### Header Parameters​

| Name          | Required | Type   | Description                                                                                         |
| ------------- | -------- | ------ | --------------------------------------------------------------------------------------------------- |
| Authorization | true     | string | Requires the format where is obtained from the [Token API](/developer/api-documentation/get-token). |
| Accept        | true     | string | Defines the content format the client expects, which should be set to .                             |

### Query Parameters​

| Name     | Required | Type   | Description                                                                                                                                                                                  |
| -------- | -------- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| order_id | true     | string | The order ID for which the order to get order trades. For the regex pattern applicable to this field, see the [Field Pattern Appendix](/developer/api-documentation/appendix/field-pattern). |

**Responses**

- 200
- 4XX

---

### Response Body​

| Name            | Type     | Description                                                                                                                                        |
| --------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| status          | string   | A string indicating the outcome of the request. Typically for successful operations.                                                               |
| data            | object[] | Response data for trades                                                                                                                           |
| data[].exchange | string   | Exchange to which the order is associated. Valid exchanges can be found in the [Exchange Appendix](/developer/api-documentation/appendix/exchange) |
| data[].product  | string   | Signifies if the order was either Intraday, Delivery or CO.                                                                                        |

Possible values: , , , .  
data[].trading_symbol| string| Shows the trading symbol which could be a combination of symbol name, instrument, expiry date etc  
data[].instrument_token| string| Key of the instrument. For the regex pattern applicable to this field, see the [Field Pattern Appendix](/developer/api-documentation/appendix/field-pattern).  
data[].order_type| string| Type of order. It can be one of the following MARKET refers to market order LIMIT refers to Limit Order SL refers to Stop Loss Limit SL-M refers to Stop Loss Market.  
Possible values: , , , .  
data[].transaction_type| string| Indicates whether its a buy or sell order.  
Possible values: , .  
data[].quantity| int32| The total quantity traded from this particular order  
data[].exchange_order_id| string| Unique order ID assigned by the exchange for the order placed  
data[].order_id| string| Unique order ID assigned internally for the order placed  
data[].exchange_timestamp| string| User readable time at when the trade occurred  
data[].average_price| float| Price at which the traded quantity is traded  
data[].trade_id| string| Trade ID generated from exchange towards traded transaction  
data[].order_ref_id| string| Uniquely identifies an order for internal usage.  
data[].order_timestamp| string| User readable timestamp at which the order was placed

Notice of Deprecation

The lowercase field () is deprecated and will be removed in future versions. Use the snake_case versions for consistency.

### Error codes​

| Error code | Description                                                                                                |
| ---------- | ---------------------------------------------------------------------------------------------------------- |
| UDAPI1023  | **Order id is required** \- Please ensure you provide an order id.                                         |
| UDAPI1010  | **Order id accepts only alphanumeric characters and '-'.** \- The order id you've provided isn't accepted. |

## Examples​

A comprehensive set of examples is provided to illustrate various use cases and implementation scenarios for this API. To view detailed examples and access sample code, please refer to: [API Examples](/developer/api-documentation/example-code/orders/get-order-trades).

Loading...

[PreviousGet Trades](/developer/api-documentation/get-trade-history)[NextGet Trade History](/developer/api-documentation/get-historical-trades)

---

## [Get Trade History | Upstox Developer API](https://upstox.com/developer/api-documentation/get-historical-trades)

- [](/developer/api-documentation/)
- [Developer API](/developer/api-documentation/open-api)
- [Orders](/developer/api-documentation/orders)
- Get Trade History

## Get Trade History​

The Trade History API provides users with access to their historical trade and transaction data, allowing them to retrieve details of orders executed through Upstox platform. This API enables various use cases, including reviewing past month's trade activity, maintaining records for compliance or analysis, and other potential use case.

NOTE

Currently this API will give you data only for last 3 financial years.

### Header Parameters​

| Name          | Required | Type   | Description                                                                                         |
| ------------- | -------- | ------ | --------------------------------------------------------------------------------------------------- |
| Authorization | true     | string | Requires the format where is obtained from the [Token API](/developer/api-documentation/get-token). |
| Accept        | true     | string | Defines the content format the client expects, which should be set to .                             |

### Query Parameters​

| Name    | Required | Type   | Description                                                                                                           |
| ------- | -------- | ------ | --------------------------------------------------------------------------------------------------------------------- |
| segment | false    | string | Segment for which data is requested can be from the following options, If not provide, will consider all the segment. |

EQ - Equity  
FO - Futures and Options  
COM - Commodity  
CD - Currency Derivatives  
MF - Mutual funds  
start_date| true| string| Date from which data needs to be fetched. it should be within the last 3 financial years. Date format: .  
end_date| true| string| Date till data needs to be fetched. it should be within the last 3 financial years. Date format: .  
page_number| true| integer| Page number, the pages are starting from 1.  
page_size| true| integer| Page size for pagination.

**Responses**

- 200
- 4XX

---

### Response Body​

- EQ
- FO
- COM
- CD
- MF

| Name            | Type     | Description                                                                                                                                        |
| --------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| status          | string   | A string indicating the outcome of the request. Typically for successful operations.                                                               |
| data            | object[] | Response data for historical trade reports                                                                                                         |
| data[].exchange | string   | Exchange to which the order is associated. Valid exchanges can be found in the [Exchange Appendix](/developer/api-documentation/appendix/exchange) |
| data[].segment  | string   | Segment to which the order is associated.                                                                                                          |

Possible values: , , , , .  
data[].option_type| string| Option type of the option contracts. Possible values: , .  
**Option type is available only in case of FO and CD segment.**  
data[].quantity| integer| Quantity with which the order was placed.  
data[].amount| float| Total amount at which order is bought/sold.  
data[].trade_id| string| Trade ID generated from exchange towards traded transaction  
data[].trade_date| string| The date on which the order was bought/sold  
data[].transaction_type| string| Indicates whether its a buy or sell order.  
Possible values: , .  
data[].scrip_name| string| Name of the scrip traded  
data[].strike_price| float| The strike price for the option.  
data[].expiry| string| Expiry date (for derivatives). Data format is .  
data[].price| float| Price at which the traded quantity is traded.  
data[].isin| string| This represents the standard ISIN for stocks listed on multiple exchanges.  
**ISIN is available in case of EQ and MF segment.**  
data[].symbol| string| Shows the trading symbol of the instrument.  
**Symbol is available in case of EQ and FO segment.**  
data[].instrument_token| string| Key of the instrument. For the regex pattern applicable to this field, see the [Field Pattern Appendix](/developer/api-documentation/appendix/field-pattern).  
**Instrument token is available in case of EQ and MF segment.**  
metadata| object| Meta data for historical trade data  
metadata.page| object| Meta data for page.  
metadata.page.page_number| integer| Page number for pagination  
metadata.page.page_size| integer| Page size

### Error codes​

| Error code | Description                                                                                                                                      |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| UDAPI1066  | **The segment is invalid** \- The provided segment value isn't recognized or accepted.                                                           |
| UDAPI1091  | **The page_number is required** \- You need to specify the page number for the data you're trying to retrieve.                                   |
| UDAPI1092  | **The page_size is required** \- The page size, indicating the number of results per page, must be provided.                                     |
| UDAPI1093  | **The start_date and end_date exceed the financial year limit.** \- Ensure your date ranges lies within the last 3 financial years.              |
| UDAPI1094  | **end_date must be greater than or equal to start_date and Date should be in valid format:** \- Ensure your date ranges and formats are correct. |

## Examples​

A comprehensive set of examples is provided to illustrate various use cases and implementation scenarios for this API. To view detailed examples and access sample code, please refer to: [API Examples](/developer/api-documentation/example-code/orders/get-historical-trades).

Loading...

[PreviousGet Order Trades](/developer/api-documentation/get-trades-by-order)[NextPortfolio](/developer/api-documentation/portfolio)

---

## [Portfolio | Upstox Developer API](https://upstox.com/developer/api-documentation/portfolio#docusaurus_skipToContent_fallback)

- [](/developer/api-documentation/)
- [Developer API](/developer/api-documentation/open-api)
- Portfolio

# Portfolio

## [description Get PositionsGet current positions of the user.](/developer/api-documentation/get-positions)## [description Convert PositionsConvert the margin product of an open position.](/developer/api-documentation/convert-positions)## [description Get HoldingsGet long term holdings of the user.](/developer/api-documentation/get-holdings)

[PreviousGet Trade History](/developer/api-documentation/get-historical-trades)[NextGet Positions](/developer/api-documentation/get-positions)

---

## [Convert Positions | Upstox Developer API](https://upstox.com/developer/api-documentation/convert-positions)

- [](/developer/api-documentation/)
- [Developer API](/developer/api-documentation/open-api)
- [Portfolio](/developer/api-documentation/portfolio)
- Convert Positions

## Convert Positions​

API to convert your intraday positions into delivery trades or your margin trades into cash and carry, and vice versa. Position would be converted only if the required margin is available. Delivery holdings can be converted to Intraday positions only if it is purchased on the same day before the [auto square off timing](https://help.upstox.com/support/solutions/articles/252251-what-is-auto-square-off-and-what-is-the-auto-square-off-timings-for-different-segments-). Only simple order can be converted from Intraday to delivery, Special orders like CO cannot be converted from intraday to delivery.

### Header Parameters​

| Name          | Required | Type   | Description                                                                                         |
| ------------- | -------- | ------ | --------------------------------------------------------------------------------------------------- |
| Authorization | true     | string | Requires the format where is obtained from the [Token API](/developer/api-documentation/get-token). |
| Content-Type  | true     | string | Indicates the media type of the resource, set as .                                                  |
| Accept        | true     | string | Defines the content format the client expects, which should be set to .                             |

### Request Body​

| Name             | Required | Type   | Description                                                                                                                                                   |
| ---------------- | -------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| instrument_token | true     | string | Key of the instrument. For the regex pattern applicable to this field, see the [Field Pattern Appendix](/developer/api-documentation/appendix/field-pattern). |
| new_product      | true     | string | Indicates the new product to use for the convert positions.                                                                                                   |

Possible values: , , .  
old_product| true| string| Indicates the old product to use for the convert positions.  
Possible values: , , .  
transaction_type| true| string| Indicates whether its a buy(b) or sell(s) order.  
Possible values: , .  
quantity| true| int32| Quantity with which the position to convert

**Responses**

- 200
- 4XX

---

### Response Body​

| Name        | Type   | Description                                                                          |
| ----------- | ------ | ------------------------------------------------------------------------------------ |
| status      | string | A string indicating the outcome of the request. Typically for successful operations. |
| data        | object | Response data for convert position request                                           |
| data.status | string | Status message for convert position request                                          |

### Error codes​

| Error code | Description                                                                                                                         |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| UDAPI1033  | **Get position data failed** \- There was an issue retrieving the position data.                                                    |
| UDAPI1034  | **Positions unavailable for given user id** \- No positions were found for the specified user ID.                                   |
| UDAPI1035  | **Positions unavailable for given instrument key or product** \- No positions match the provided instrument key or product details. |

## Examples​

A comprehensive set of examples is provided to illustrate various use cases and implementation scenarios for this API. To view detailed examples and access sample code, please refer to: [API Examples](/developer/api-documentation/example-code/portfolio/convert-positions).

Loading...

[PreviousGet Positions](/developer/api-documentation/get-positions)[NextGet Holdings](/developer/api-documentation/get-holdings)

---

## [Trade Profit And Loss | Upstox Developer API](https://upstox.com/developer/api-documentation/trade-profit-and-loss#docusaurus_skipToContent_fallback)

- [](/developer/api-documentation/)
- [Developer API](/developer/api-documentation/open-api)
- Trade Profit And Loss

# Trade Profit And Loss

## [description Get Report Meta DataGet report meta data.](/developer/api-documentation/get-report-meta-data)## [description Get Profit Loss ReportGet profit and loss report.](/developer/api-documentation/get-profit-and-loss-report)## [description Get Trades ChargesGet trade charges.](/developer/api-documentation/get-trade-charges)

[PreviousGet Holdings](/developer/api-documentation/get-holdings)[NextGet Report Meta Data](/developer/api-documentation/get-report-meta-data)

---

## [Get Profit And Loss Meta Data On Trades | Upstox Developer API](https://upstox.com/developer/api-documentation/get-report-meta-data)

- [](/developer/api-documentation/)
- [Developer API](/developer/api-documentation/open-api)
- [Trade Profit And Loss](/developer/api-documentation/trade-profit-and-loss)
- Get Report Meta Data

## Get Report Meta Data​

### Header Parameters​

| Name          | Required | Type   | Description                                                                                         |
| ------------- | -------- | ------ | --------------------------------------------------------------------------------------------------- |
| Authorization | true     | string | Requires the format where is obtained from the [Token API](/developer/api-documentation/get-token). |
| Accept        | true     | string | Defines the content format the client expects, which should be set to .                             |

### Query Parameters​

| Name           | Required | Type   | Description                                                                                                                                                                                                                                                                                         |
| -------------- | -------- | ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| from_date      | false    | string | Date from which data needs to be fetched. from_date and to_date should fall under the same financial year as mentioned in financial_year attribute. Date in dd-mm-yyyy format                                                                                                                       |
| to_date        | false    | string | Date till which data needs to be fetched. from_date and to_date should fall under the same financial year as mentioned in financial_year attribute. Date in dd-mm-yyyy format                                                                                                                       |
| segment        | true     | string | Segment for which data is requested can be from the following options EQ - Equity, FO - Futures and Options, COM - Commodity, CD - Currency Derivatives                                                                                                                                             |
| financial_year | true     | string | Financial year for which data has been requested. Concatenation of last 2 digits of from year and to year Sample:for 2021-2022, financial_year will be 2122. For the regex pattern applicable to this field, see the [Field Pattern Appendix](/developer/api-documentation/appendix/field-pattern). |

**Responses**

- 200
- 4XX

---

### Response Body​

| Name                 | Type    | Description                                                                          |
| -------------------- | ------- | ------------------------------------------------------------------------------------ |
| status               | string  | A string indicating the outcome of the request. Typically for successful operations. |
| data                 | object  | Response data for brokerage                                                          |
| data.trades_count    | integer | Total count of trades in the trade wise P and L report                               |
| data.page_size_limit | integer | Maximum number of trades in a page of the trade wise P and L report API              |

### Error codes​

| Error code  | Description                                                                                                                                               |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| UDAPI1067   | **The 'segment' is required** \- You must provide the 'segment' for this operation.                                                                       |
| UDAPI1066   | **The 'segment' is invalid** \- The provided 'segment' value isn't recognized or accepted.                                                                |
| UDAPI1070   | **The financial_year is required** \- Please specify the 'financial_year' in your request.                                                                |
| UDAPI1074   | **The financial_year is invalid** \- The 'financial_year' you've provided isn't recognized or valid.                                                      |
| UDAPI100051 | **Invalid financial year** \- The financial year you've entered doesn't match any recognized formats or values.                                           |
| UDAPI1075   | **to_date must be greater than or equal to from_date and Date should be in valid format: dd-mm-yyyy** \- Ensure your date ranges and formats are correct. |

## Examples​

A comprehensive set of examples is provided to illustrate various use cases and implementation scenarios for this API. To view detailed examples and access sample code, please refer to: [API Examples](/developer/api-documentation/example-code/trade-profit-and-loss/get-report-meta-data).

Loading...

[PreviousTrade Profit And Loss](/developer/api-documentation/trade-profit-and-loss)[NextGet Profit Loss Report](/developer/api-documentation/get-profit-and-loss-report)

---

## [Get Trade-wise Profit and Loss Report Data | Upstox Developer API](https://upstox.com/developer/api-documentation/get-profit-and-loss-report)

- [](/developer/api-documentation/)
- [Developer API](/developer/api-documentation/open-api)
- [Trade Profit And Loss](/developer/api-documentation/trade-profit-and-loss)
- Get Profit Loss Report

## Get Profit Loss Report​

### Header Parameters​

| Name          | Required | Type   | Description                                                                                         |
| ------------- | -------- | ------ | --------------------------------------------------------------------------------------------------- |
| Authorization | true     | string | Requires the format where is obtained from the [Token API](/developer/api-documentation/get-token). |
| Accept        | true     | string | Defines the content format the client expects, which should be set to .                             |

### Query Parameters​

| Name           | Required | Type            | Description                                                                                                                                                                                                                                                                                         |
| -------------- | -------- | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| from_date      | false    | string          | Date from which data needs to be fetched. from_date and to_date should fall under the same financial year as mentioned in financial_year attribute. Date in dd-mm-yyyy format                                                                                                                       |
| to_date        | false    | string          | Date till which data needs to be fetched. from_date and to_date should fall under the same financial year as mentioned in financial_year attribute. Date in dd-mm-yyyy format                                                                                                                       |
| segment        | true     | string          | Segment for which data is requested can be from the following options EQ - Equity, FO - Futures and Options, COM - Commodity, CD - Currency Derivatives                                                                                                                                             |
| financial_year | true     | string          | Financial year for which data has been requested. Concatenation of last 2 digits of from year and to year Sample:for 2021-2022, financial_year will be 2122. For the regex pattern applicable to this field, see the [Field Pattern Appendix](/developer/api-documentation/appendix/field-pattern). |
| page_number    | true     | integer (int32) | Page Number, the pages are starting from 1                                                                                                                                                                                                                                                          |
| page_size      | true     | integer (int32) | Page size for pagination. The maximum page size value is obtained from P and L report metadata API.                                                                                                                                                                                                 |

**Responses**

- 200
- 4XX

---

### Response Body​

| Name                      | Type     | Description                                                                          |
| ------------------------- | -------- | ------------------------------------------------------------------------------------ |
| status                    | string   | A string indicating the outcome of the request. Typically for successful operations. |
| data                      | object[] | Response data for trade wise data details                                            |
| data[].quantity           | float    | The quantity of stock traded                                                         |
| data[].isin               | string   | ISIN of the stock                                                                    |
| data[].scrip_name         | string   | Name of the scrip traded                                                             |
| data[].trade_type         | string   | FUT - Futures OPT - Options EQ - Equity                                              |
| data[].buy_date           | string   | The date on which the stock was bought                                               |
| data[].buy_average        | float    | The average rate at which each quantity of the stock was bought                      |
| data[].sell_date          | string   | The date on which the stock was sold                                                 |
| data[].sell_average       | float    | The average rate at which each quantity of the stock was sold                        |
| data[].buy_amount         | float    | Total buy amount                                                                     |
| data[].sell_amount        | float    | Total sell amount                                                                    |
| metadata                  | object   | Meta data for trade wise data details                                                |
| metadata.page             | object   | Meta data for page.                                                                  |
| metadata.page.page_number | int32    | pageNumber for pagination                                                            |
| metadata.page.page_size   | int32    | Page size                                                                            |

### Error codes​

| Error code  | Description                                                                                                                                               |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| UDAPI1067   | **The 'segment' is required** \- You must provide the 'segment' for this operation.                                                                       |
| UDAPI1066   | **The 'segment' is invalid** \- The provided 'segment' value isn't recognized or accepted.                                                                |
| UDAPI1070   | **The financial_year is required** \- Please specify the 'financial_year' in your request.                                                                |
| UDAPI1074   | **The financial_year is invalid** \- The 'financial_year' you've provided isn't recognized or valid.                                                      |
| UDAPI1071   | **The page_number is required** \- You need to specify the page number for the data you're trying to retrieve.                                            |
| UDAPI1072   | **The page_size is required** \- The page size, indicating the number of results per page, must be provided.                                              |
| UDAPI100051 | **Invalid financial year** \- The financial year you've entered doesn't match any recognized formats or values.                                           |
| UDAPI1075   | **to_date must be greater than or equal to from_date and Date should be in valid format: dd-mm-yyyy** \- Ensure your date ranges and formats are correct. |

## Examples​

A comprehensive set of examples is provided to illustrate various use cases and implementation scenarios for this API. To view detailed examples and access sample code, please refer to: [API Examples](/developer/api-documentation/example-code/trade-profit-and-loss/get-profit-loss-report).

Loading...

[PreviousGet Report Meta Data](/developer/api-documentation/get-report-meta-data)[NextGet Trades Charges](/developer/api-documentation/get-trade-charges)

---

## [Get Profit And Loss On Trades | Upstox Developer API](https://upstox.com/developer/api-documentation/get-trade-charges)

- [](/developer/api-documentation/)
- [Developer API](/developer/api-documentation/open-api)
- [Trade Profit And Loss](/developer/api-documentation/trade-profit-and-loss)
- Get Trades Charges

## Get Trades Charges​

### Header Parameters​

| Name          | Required | Type   | Description                                                                                         |
| ------------- | -------- | ------ | --------------------------------------------------------------------------------------------------- |
| Authorization | true     | string | Requires the format where is obtained from the [Token API](/developer/api-documentation/get-token). |
| Accept        | true     | string | Defines the content format the client expects, which should be set to .                             |

### Query Parameters​

| Name           | Required | Type   | Description                                                                                                                                                                                                                                                                                         |
| -------------- | -------- | ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| from_date      | false    | string | Date from which data needs to be fetched. from_date and to_date should fall under the same financial year as mentioned in financial_year attribute. Date in dd-mm-yyyy format                                                                                                                       |
| to_date        | false    | string | Date till which data needs to be fetched. from_date and to_date should fall under the same financial year as mentioned in financial_year attribute. Date in dd-mm-yyyy format                                                                                                                       |
| segment        | true     | string | Segment for which data is requested can be from the following options EQ - Equity, FO - Futures and Options, COM - Commodity, CD - Currency Derivatives                                                                                                                                             |
| financial_year | true     | string | Financial year for which data has been requested. Concatenation of last 2 digits of from year and to year Sample:for 2021-2022, financial_year will be 2122. For the regex pattern applicable to this field, see the [Field Pattern Appendix](/developer/api-documentation/appendix/field-pattern). |

**Responses**

- 200
- 4XX

---

### Response Body​

| Name                                             | Type   | Description                                                                          |
| ------------------------------------------------ | ------ | ------------------------------------------------------------------------------------ |
| status                                           | string | A string indicating the outcome of the request. Typically for successful operations. |
| data                                             | object | Response data for brokerage                                                          |
| data.charges_breakdown                           | object | Response data for charges details                                                    |
| data.charges_breakdown.total                     | float  | Total charges for the user                                                           |
| data.charges_breakdown.brokerage                 | float  | Brokerage charges for the order                                                      |
| data.charges_breakdown.taxes                     | object | Taxes levied on order                                                                |
| data.charges_breakdown.taxes.gst                 | float  | GST charges                                                                          |
| data.charges_breakdown.taxes.stt                 | float  | STT charges                                                                          |
| data.charges_breakdown.taxes.stamp_duty          | float  | Stamp duty charges                                                                   |
| data.charges_breakdown.charges                   | object | Other charges levied                                                                 |
| data.charges_breakdown.charges.transaction       | float  | transaction charges                                                                  |
| data.charges_breakdown.charges.clearing          | float  | clearing charges                                                                     |
| data.charges_breakdown.charges.ipft              | float  | IPF charges                                                                          |
| data.charges_breakdown.charges.others            | float  | others charges                                                                       |
| data.charges_breakdown.charges.sebi_turnover     | float  | SEBI turnover                                                                        |
| data.charges_breakdown.charges.demat_transaction | float  | demat transaction charges                                                            |

### Error codes​

| Error code  | Description                                                                                                                                               |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| UDAPI1067   | **The 'segment' is required** \- You must provide the 'segment' for this operation.                                                                       |
| UDAPI1066   | **The 'segment' is invalid** \- The provided 'segment' value isn't recognized or accepted.                                                                |
| UDAPI1070   | **The financial_year is required** \- Please specify the 'financial_year' in your request.                                                                |
| UDAPI1074   | **The financial_year is invalid** \- The 'financial_year' you've provided isn't recognized or valid.                                                      |
| UDAPI100051 | **Invalid financial year** \- The financial year you've entered doesn't match any recognized formats or values.                                           |
| UDAPI1075   | **to_date must be greater than or equal to from_date and Date should be in valid format: dd-mm-yyyy** \- Ensure your date ranges and formats are correct. |

## Examples​

A comprehensive set of examples is provided to illustrate various use cases and implementation scenarios for this API. To view detailed examples and access sample code, please refer to: [API Examples](/developer/api-documentation/example-code/trade-profit-and-loss/get-trade-charges).

Loading...

[PreviousGet Profit Loss Report](/developer/api-documentation/get-profit-and-loss-report)[NextHistorical Data](/developer/api-documentation/historical-data)

---

## [Historical Data | Upstox Developer API](https://upstox.com/developer/api-documentation/historical-data#docusaurus_skipToContent_fallback)

- [](/developer/api-documentation/)
- [Developer API](/developer/api-documentation/open-api)
- Historical Data

# Historical Data

## [description Historical Candle DataGet historical OHLC values for the given instrument.](/developer/api-documentation/get-historical-candle-data)## [description Intraday Candle DataGet present trading day OHLC values for the given instrument.](/developer/api-documentation/get-intra-day-candle-data)

[PreviousGet Trades Charges](/developer/api-documentation/get-trade-charges)[NextHistorical Candle Data](/developer/api-documentation/get-historical-candle-data)

---

## [Historical Candle Data | Upstox Developer API](https://upstox.com/developer/api-documentation/get-historical-candle-data)

- [](/developer/api-documentation/)
- [Developer API](/developer/api-documentation/open-api)
- [Historical Data](/developer/api-documentation/historical-data)
- Historical Candle Data

## Historical Candle Data​

API to retrieve OHLC (Open, High, Low, Close) data for instruments spanning multiple timeframes. Historical data is available for the following time durations:

- 1-minute: Retrieve the candles from the final month leading up to the endDate.
- 30-minute: Retrieve the candles from the past year up to the endDate.
- Daily: Retrieve data for the past year, concluding on the endDate.
- Weekly: Retrieve data from the previous ten years, ending on the endDate.
- Monthly: Retrieve data spanning the last ten years, up to the specified endDate.

NOTE

- Use the [Intraday API](/developer/api-documentation/get-intra-day-candle-data) to retrieve data specific to the current trading day.
- One-minute and 30-minute candle data are accessible solely for the preceding six months.
- It's important to note that parameter accepts only a single identifier per request; comma-separated values or multiple identifiers are not supported.

### Header Parameters​

| Name   | Required | Type   | Description                                                             |
| ------ | -------- | ------ | ----------------------------------------------------------------------- |
| Accept | true     | string | Defines the content format the client expects, which should be set to . |

### Path Parameters​

| Name           | Required | Type   | Description                                                                                                                                                                                                                           |
| -------------- | -------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| instrument_key | true     | string | The unique identifier for the financial instrument for which historical data is being queried. For the regex pattern applicable to this field, see the [Field Pattern Appendix](/developer/api-documentation/appendix/field-pattern). |
| interval       | true     | string | Specifies the time frame of the candles.                                                                                                                                                                                              |

Possible values: , , , , .  
to_date| true| string| The ending date (inclusive) for the historical data range. Format: 'YYYY-MM-DD'.  
from_date| false| string| The starting date for the historical data range. Format: 'YYYY-MM-DD'.

**Responses**

- 200
- 4XX

---

### Response Body​

| Name           | Type    | Description                                                                                              |
| -------------- | ------- | -------------------------------------------------------------------------------------------------------- |
| status         | string  | A string indicating the outcome of the request. Typically for successful operations.                     |
| data           | object  | Contains OHLC values for all instruments across various timeframes.                                      |
| data.candles   | array[] | Array of candle data, each presented as an array with sequential elements representing trading activity. |
| data.candle[0] | number  | : Indicating the start time of the candle's timeframe.                                                   |
| data.candle[1] | number  | : The opening price of the asset for the given timeframe.                                                |
| data.candle[2] | number  | : The highest price at which the asset traded during the timeframe.                                      |
| data.candle[3] | number  | : The lowest price at which the asset traded during the timeframe.                                       |
| data.candle[4] | number  | : The closing price of the asset for the given timeframe.                                                |
| data.candle[5] | number  | : The total amount of the asset that was traded during the timeframe.                                    |
| data.candle[6] | number  | : The total number of outstanding derivative contracts, such as options or futures.                      |

### Error codes​

| Error code  | Description                                                                                                            |
| ----------- | ---------------------------------------------------------------------------------------------------------------------- |
| UDAPI1021   | **Instrument key is of invalid format** \- The provided instrument key doesn't conform to the expected format.         |
| UDAPI1020   | **Interval accepts one of (1minute,30minute,day,week,month)** \- Ensure the 'interval' is one of the specified values. |
| UDAPI1022   | **to_date is required** \- You must specify the 'to_date' in your request.                                             |
| UDAPI100011 | **Invalid Instrument key** \- The instrument key you provided doesn't match any of the recognized keys in the system.  |

## Examples​

A comprehensive set of examples is provided to illustrate various use cases and implementation scenarios for this API. To view detailed examples and access sample code, please refer to: [API Examples](/developer/api-documentation/example-code/historical-data/historical-candle-data).

Loading...

[PreviousHistorical Data](/developer/api-documentation/historical-data)[NextIntraday Candle Data](/developer/api-documentation/get-intra-day-candle-data)

---

## [Intraday Candle Data | Upstox Developer API](https://upstox.com/developer/api-documentation/get-intra-day-candle-data)

- [](/developer/api-documentation/)
- [Developer API](/developer/api-documentation/open-api)
- [Historical Data](/developer/api-documentation/historical-data)
- Intraday Candle Data

## Intraday Candle Data​

API to retrieve OHLC (Open, High, Low, Close) values for instruments during the current trading day. Data is accessible for 1-minute and 30-minute intervals from the beginning of the market session. For real-time candlestick updates, it is advisable to utilize the [Market Update Stream](/developer/api-documentation/get-market-data-feed).

NOTE

- It's important to note that parameter accepts only a single identifier per request; comma-separated values or multiple identifiers are not supported.
- A minor delay may be experienced in the delivery of the most recent candle data, attributable to CDN caching. For immediate access to the latest data, it is advisable to connect to the websocket endpoints.

### Header Parameters​

| Name   | Required | Type   | Description                                                             |
| ------ | -------- | ------ | ----------------------------------------------------------------------- |
| Accept | true     | string | Defines the content format the client expects, which should be set to . |

### Path Parameters​

| Name           | Required | Type   | Description                                                                                                                                                                                                                           |
| -------------- | -------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| instrument_key | true     | string | The unique identifier for the financial instrument for which historical data is being queried. For the regex pattern applicable to this field, see the [Field Pattern Appendix](/developer/api-documentation/appendix/field-pattern). |
| interval       | true     | string | Specifies the time frame of the candles.                                                                                                                                                                                              |

Possible values: , .

**Responses**

- 200
- 4XX

---

### Response Body​

| Name           | Type    | Description                                                                                              |
| -------------- | ------- | -------------------------------------------------------------------------------------------------------- |
| status         | string  | A string indicating the outcome of the request. Typically for successful operations.                     |
| data           | object  | Contains OHLC values for all instruments across various timeframes.                                      |
| data.candles   | array[] | Array of candle data, each presented as an array with sequential elements representing trading activity. |
| data.candle[0] | number  | : Indicating the start time of the candle's timeframe.                                                   |
| data.candle[1] | number  | : The opening price of the asset for the given timeframe.                                                |
| data.candle[2] | number  | : The highest price at which the asset traded during the timeframe.                                      |
| data.candle[3] | number  | : The lowest price at which the asset traded during the timeframe.                                       |
| data.candle[4] | number  | : The closing price of the asset for the given timeframe.                                                |
| data.candle[5] | number  | : The total amount of the asset that was traded during the timeframe.                                    |
| data.candle[6] | number  | : The total number of outstanding derivative contracts, such as options or futures.                      |

### Error codes​

| Error code  | Description                                                                                                            |
| ----------- | ---------------------------------------------------------------------------------------------------------------------- |
| UDAPI1021   | **Instrument key is of invalid format** \- The provided instrument key doesn't conform to the expected format.         |
| UDAPI1020   | **Interval accepts one of (1minute,30minute,day,week,month)** \- Ensure the 'interval' is one of the specified values. |
| UDAPI100011 | **Invalid Instrument key** \- The instrument key you provided doesn't match any of the recognized keys in the system.  |

## Examples​

A comprehensive set of examples is provided to illustrate various use cases and implementation scenarios for this API. To view detailed examples and access sample code, please refer to: [API Examples](/developer/api-documentation/example-code/historical-data/intra-day-candle-data).

Loading...

[PreviousHistorical Candle Data](/developer/api-documentation/get-historical-candle-data)[NextMarket Quote](/developer/api-documentation/market-quote)

---
