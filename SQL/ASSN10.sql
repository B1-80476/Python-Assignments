1. Write a procedure that computes the perimeter and the area of a
rectangle. Define your own values for the length and width. (Assuming
that L and W are the length and width of the rectangle, Perimeter =
2*(L+W) and Area = L*W.

-->

DROP procedure if exists sp_rectangle;

delimiter $$

create procedure sp_rectangle(IN L int, IN W int)
BEGIN

declare r_area double;
declare r_parameter double;

set r_area = L*W;
set r_parameter = 2*(L+W);

insert into result values (r_area, 'area of rectangle');
insert into result values (r_parameter, 'parameter of rectangle');

END;
$$

delimiter ;

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
2. Write a procedure that declares an integer variable called num,
assigns a value to it, and computes and inserts into the temp table
the value of the variable itself, its square, and its cube.

-->

DROP procedure if exists sp_sqcu;

delimiter $$

create procedure sp_sqcu(IN num int)
BEGIN

declare num_sqr double;
declare num_cube double;

set num_sqr = num * num;
set num_cube = num * num * num;

insert into temp values (num_sqr, 'SQUARE');
insert into temp values (num_cube, 'CUBE');

END;
$$

delimiter ;



---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
3.Create a procedure to Convert a temperature in Fahrenheit (F) to its
equivalent in Celsius (C) and vice versa. The required formulae are:-
C= (F-32)*5/9 F= 9/5*C + 32.

-->

DROP procedure if exists sp_CF;

delimiter $$

create procedure sp_CF(IN C int, IN F int)
BEGIN

declare Fahrenheit double;
declare Celsius double;

set Fahrenheit = 9/5*C + 32;
set Celsius = (F-32)*5/9;

insert into temper values (Fahrenheit, 'celsius to fahrenheit');
insert into temper values (Celsius, 'fahrenheit to celsius');

END;
$$

delimiter ;


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
4.Create a procedure to Convert a number of inches into yards, feet,
and inches. For example, 124 inches equals 3 yards, 1 foot, and 4
inches.

-->

DROP procedure if exists sp_CF;

delimiter $$

create procedure sp_CF(IN inc int)
BEGIN

declare yard double;
declare remaining_inches double;
declare foot double;
declare remaining double;
declare inch double;

set yard = inc / 36;
set remaining_inches = inc % 36;
set foot  = remaining_inches/12;
set inch = remaining_inches % 12;

insert into area values (yard,foot,inch, 'inch conversion');

END;
$$

delimiter ;


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
5. Your block should read in two real numbers and tell whether the
product of the two numbers is equal to or greater than 100.

-->

DROP procedure if exists sp_real;

delimiter $$

create procedure sp_real(IN A int,IN B int)
BEGIN

declare product double;

set product = A * B;

IF product>=100 THEN
select product as `greater or eqal to 100`;
END IF;

END;
$$

delimiter ;