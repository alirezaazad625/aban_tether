## Run & Test

- Serve application with `make up` command serves web server on port `5000` and runs worker.

## Considerations

- In the current project I used `SQLite` database which can be replaced by `MySQL` easily(because I used `SQLAlchemy` and the
  interface supports both just by changing the configuration in [`src/configs/database.py`](src/configs/database.py) we can connect to `MySQL`).
- There is a worker which uses `scheduler` and periodically gets not purchased transactions and performs the remained
  action.

## Existing Issues

- It's recommended for production deployment to use `WSGI`.
- Because of not mentioned in the documentation I did not implement any authorization and authentication, but it is
  necessary.
- Error handling(errors not handled therefore the returned errors to users might be unclear and obscure).
- I did not use dependency injection but if the project is going to grow it's better to implement it.
- On [`buy_from_exchange`](src/exchange/application/exchange_service.py) could be errors that our system is not being updated which results in duplicate purchases or other
  issues(because now we are using mock nothing bad happens but if we are going to connect it to a third party this problem
  is not far away).
- There are no validations on coin names.
