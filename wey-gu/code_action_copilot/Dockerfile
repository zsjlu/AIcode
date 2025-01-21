# add one extra binary to the netshoot image, the binary comes from 
# vesoft/nebula-console:v3 and the path is /usr/local/nebula-console/bin/nebula

FROM nicolaka/netshoot:latest

# copy /usr/local/nebula-console/bin/nebula from image: vesoft/nebula-console:v3
COPY --from=vesoft/nebula-console:v3 /usr/local/nebula-console/bin/nebula /usr/local/nebula-console/bin/nebula  