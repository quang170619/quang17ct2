# webappnorthwind
##connect server
# nguyenngocha17ct2
## Lê Hà Quang
## Nguyễn Thị Yến
## Hồ Văn Nhật


#docker 
https://docs.docker.com/v17.09/get-started/part2/#dockerfile


# backend
# docker build -t backend .

# docker run -d --name backend --env db_ip=172.17.0.2 -p 8080:8080 backend 
172.17.0.2 ( ip của cổng 5432) docker inspect coredb
172.17.86.33:8080 ( chạy bên postman)

# docker exec -it coredb bash


# psql -U postgres
# \l
# create database KTgiuaki;
# \c xyz;
# \c KTgiuaki;
# \dt
# select * from tblcustomers;
# select * from Categories;
# select * from Employees ,OrderDetails , Orders , Products, Shippers, Suppliers

# sudo docker stop backend
# sudo docker rm backend 

# deploy db
 sudo docker load --input postgres_11.2-alpine.tar

 sudo docker run -d --restart unless-stopped --name coredb -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=postgres -v ~/northwind_db:/var/lib/postgresql/data -p 5432:5432 postgres:11.2-alpine
