Note : use “sales” database to solve below queries.


1. Create an index that will enable a user to pull orders for ‘1990-10-03’ out of the
Orders table quickly.

mysql> create index idx_orders_odate ON orders(odate);



2. If the Orders table has already been created, how can you force the onum field to be
unique (assume all current values are unique)?

 create unique index inx_orders_onum ON orders(onum);



3. Create an index that would permit salesperson to retrieve his orders.

mysql> create index idx_orders ON orders(snum,onum);



4. Let us assume that each salesperson is to have only one customer of a given rating,
and that this is currently the case. Create an index that enforces it.

create unique index inx_customers_cnum_rating_snum ON orders(snum,cnum);



5. Create an index to speed up searching order on a given date by given customer.

mysql> create index inx_orders ON orders(odate,cnum);
