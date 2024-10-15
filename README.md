simple flask app with GET and POST methods(also database postgresql)
ttrying do docker-compose
how run this stuff:
  1. download this repo
  2. install docker-compose
  3. CMD: sudo docker-compose up --build
  4. how check: 1. CMD: curl -X POST http://localhost:5000/users -H "Content-Type: application/json" -d '{"name": "John Doe"}'
                2. CMD: curl http://localhost:5000/users
if you dont see message ERROR in to the container, its work
