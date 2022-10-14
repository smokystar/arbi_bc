import psycopg2
con = psycopg2.connect(user="udzclombmplopn",
                                password="006bbc0a282a6a60d71ab63eceb99327b4c73794c97b3e968d74de449d939e4d",
                                host="ec2-54-155-129-189.eu-west-1.compute.amazonaws.com",
                                port="5432",
                                database="d9tf4mansnquj2")
cur = con.cursor()