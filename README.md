The initial approach was to separate the WebAPIs into StatisticsAPI and DeviceRegistrationAPI each with their own source code, deployment, service, dockerfile, image and then I would add ingress to expose the services and netowrk policies for security with the respective secrets. 
Generally each service is simple and straightforward, isolated, potentially easier to manage if the scope remains small. Each service can be scaled and maintained independently. But it would have a lot a duplicated code, especially for apis that are closely related.
For a theoritical scenario that the application would grow, by adding more endpoints or functionality, managing these could become more complex, might have overlap between them thus inefficient resource utilisation. Then we might have consistency problems across data models, business logic etc

The latest approach was to organise it into a single project that has to do eveything related to Device Type Metrics specifically. Code can be reused, offers common functionality, models can be shared, easier to maintain, to read and it is consistent. Maybe scaling would be harder, single point of failure.
We could have a service mesh like istio to use Destionation Rules, Virtual Services and Autharisation Policies for the endpoints and application level security with keycloak or other Level 7 authentication. Network Policeis would be hard to implement.

Changed the default values for postgresql chart to be accessible from specific nodes and not be available externally. Added simple pipeline to create a docker image and push it to [docker hub](https://hub.docker.com/repositories/dbnmrs). Helm chart for the application for the ease of deployment. And tried to integrate it with Keycloak. Implemented in python with fastAPI

How to use
```
 curl -X POST "http://<external-ip>:8000/Log/auth" -H "accept: application/json" -H "Content-Type: application/json" -d '{"userKey": "testUser", "deviceType": "testDevice"}'
```
