### Quick Start

#### Simple run with docker-compose:

* Clone repository
* cd to project directory
* Run `docker-compose run web python manage.py migrate` for initialize database
* Run `docker-compose up`

After this steps service will be up.
Go to `http://127.0.0.1:8000/api/v1/` for check service is working.

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
