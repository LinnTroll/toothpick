### Quick Start

#### Live example

* [API serer](https://toothpickshare-api.herokuapp.com/)
* [Client](https://toothpickshare-client.herokuapp.com/)

#### Simple run with docker-compose

* Clone repository
* cd to project directory
* Run `docker-compose run web python manage.py migrate` for initialize database
* Run `docker-compose up`

After this steps service will be up.
Go to `http://127.0.0.1:8000/api/v1/` for check service is working.

#### Use client

Simple realisation of toothpick API client placed in file simpleclient.html.
If you run API server on http://127.0.0.1:8000, you can open this file in browser and it will be work.
If API server has another host, change BASE_API_URL option in simpleclient.html.

### REST API documentaton

#### Owners list
Returns list of all toothpick owners

* **URL**
  /api/v1/owner/

* **Method:**

  `GET`

* **Success Response:**

  **Code:** 200

  **Example:**
  ```
  [
    {
      "id": 1,
      "username": "admin",
      "first_name": "Super",
      "last_name": "Admin"
    },
    ...
  ]
  ```

#### Toothpicks list
Returns list of all toothpicks

* **URL**
  /api/v1/toothpick/

* **Methods:**

  `GET`

* **Success Response:**

  **Code:** 200

  **Example:**
  ```
  [
    {
      "id": 2,
      "serial_number": "ZB 0315888823",
      "name": "Северная 28",
      "owners": [
        {
          "id": 8,
          "username": "vasiliygupalo",
          "first_name": "Vasiliy",
          "last_name": "Gupalo"
        },
        ...
      ],
      "owners_history": [
        {
          "own_start_at": "2017-01-01T00:00:00Z",
          "own_end_at": null,
          "user": {
            "id": 8,
            "username": "vasiliygupalo",
            "first_name": "Vasiliy",
            "last_name": "Gupalo"
          }
        }
        ...
      ]
    },
    ...
  ]
  ```

#### Toothpick create
Add new toothpick to database and return it

* **URL**
  /api/v1/toothpick/

* **Methods:**

  `POST`

* **Data Params**

  ```
  {
    "serial_number": "Unique number",
    "name": "Some name",
    "owners_ids": [1, 3]
  }
  ```

* **Success Response:**

  **Code:** 200

#### Toothpick update
Update exists toothpick instance

* **URL**
  /api/v1/toothpick/:id/

* **Methods:**

  `PUT`

* **Data Params**

  ```
  {
    "serial_number": "Unique number",
    "name": "Some name",
    "owners_ids": [1, 3]
  }
  ```

* **Success Response:**

  **Code:** 200
