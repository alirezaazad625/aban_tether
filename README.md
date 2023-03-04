## Run & Test

- Serve application with `make up` command serves web server on port `5000` and runs worker.

## Considerations

- In current project I used `SQLite` database which can be replaced by mysql easily(because I used `SQLAlchemy` and the
  interface supports both just by changing the configuration in `src/configs/database.py` we can connect to `MySQL`).
- There is a worker which use `scheduler` and periodically gets not purchased transactions and perform the remained
  action.

## Existing Issues

- It's recommended for production deploy to use `WSGI`.
- Because of not mentioning in the documentation I did not implement any authorization and authentication, but it is
  necessary.
- Error handling(errors not handled therefore the returned errors to users might be unclear and obscure).
- I did not use dependency injection but if project is going to grow it's better to implement it.
- On `buy_from_exchange` could be errors that our system not be updated which results in duplicate purchases or other
  issues(because now we are using mock nothing bad happens but if we are going to connect it a third party this problem
  is not far away).
- There are no validations on coin names.