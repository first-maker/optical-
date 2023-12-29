--  to delet iteam
DELETE
FROM
    payment
where
    address_id =2
DELETE FROM producat where branch_id <1000-- to deleat table
DROP TABLE IF EXISTS usercontent;
-- to delat 
ALTER TABLE users DROP brand_type
--  to add

ALTER TABLE producat
  ADD ModelName text DEFAULT 0;
DROP TABLE IF EXISTS order_stat;
DROP TABLE IF EXISTS order_stat;

CREATE TABLE users (
    user_id INTEGER PRIMARY KEY,
    user_name TEXT NOT NULL,
    first_name TEXT ,
    last_name TEXT,
    email TEXT NOT NULL UNIQUE,
    phone TEXT NOT NULL UNIQUE,
    wallet INTEGER
    hash TEXT NOT NULL UNIQUE
);

-- CREATE TABLE groups (
--     group_id INTEGER PRIMARY KEY,
--     name TEXT NOT NULL
-- );
-- CREATE TABLE contact_groups(
--     contact_id INTEGER,
--     group_id INTEGER,
--     PRIMARY KEY (contact_id, group_id),
--     FOREIGN KEY (contact_id) REFERENCES contacts (contact_id) ON DELETE CASCADE ON UPDATE NO ACTION,
--     FOREIGN KEY (group_id) REFERENCES groups (group_id) ON DELETE CASCADE ON UPDATE NO ACTION
-- );
-- updat done   
-- creat producat conatc table
-- CREATE TABLE usercontent (
--     content_id INTEGER PRIMARY KEY,
--     date_time DATETIME DEFAULT CURRENT_TIMESTAMP,
--     imagelink TEXT,
--     caption TEXT,
--     pric INTEGER,
--     disount INTEGER,
--     type TEXT,

--     user_id INTEGER,
--     FOREIGN KEY (user_id) REFERENCES users(user_id)ON DELETE CASCADE ON UPDATE NO ACTION
-- );
CREATE TABLE addMedia (
    media_id INTEGER PRIMARY KEY,
    date_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    imagelink TEXT,
    product_type TEXT,
    media_description TEXT,
    product_id INTEGER,
    Show_stat TEXT,
    user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE ON UPDATE NO ACTION FOREIGN KEY (product_id) REFERENCES product(product_id) ON DELETE CASCADE ON UPDATE NO ACTION
);

CREATE TABLE order_trak (
    order_id INTEGER PRIMARY KEY,
    order_number INTEGER,
    date_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    stat TEXT NOT NULL,
    notes TEXT NOT NULL,
    user_id INTEGER,
    payment_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE ON UPDATE NO ACTION,
    FOREIGN KEY (payment_id) REFERENCES payment(payment) ON DELETE CASCADE ON UPDATE NO ACTION
);

CREATE TABLE branchs(
    branch_id INTEGER PRIMARY KEY DEFAULT 1000,
    branch_name INTEGER,
    start_date_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    branch_type text,
    branch_stat text,
    user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE ON UPDATE NO ACTION
);

-- add company tabel 
CREATE TABLE company (
    company_id INTEGER NOT NULL PRIMARY KEY,
    date_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    company_name TEXT,
    company_email TEXT,
    company_tell TEXT,
    commercialNo TEXT,
    vat_no TEXT,
    company_type Text,
    company_address TEXT,
    user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE ON UPDATE NO ACTION
);

-- add Brand tabel 
CREATE TABLE brand (
    brand_id INTEGER NOT NULL PRIMARY KEY,
    date_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    brand_name TEXT,
    brand_type TEXT,
    manufactory TEXT,
    brand_description TEXT,
    user_id INTEGER,
    company_id INTEGER,
    FOREIGN KEY(company_id) REFERENCES company(company_id) ON DELETE CASCADE ON UPDATE NO ACTION,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE ON UPDATE NO ACTION
);

CREATE TABLE product(
    product_id INTEGER NOT NULL PRIMARY KEY,
    date_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    item_description TEXT,
    discount INTEGER,
    retialPrice INTEGER,
    wholePrice INTEGER,
    quant INTEGER,
    Collection_name TEXT,
    SKUCode TEXT,
    UPCcode TEXT,
    temple_length TEXT,
    lens_size TEXT,
    bridge_size TEXT,
    color TEXT,
    Model_no TEXT,
    brand_type TEXT,
    brand_id INTEGER,
    company_id INTEGER,
    user_id INTEGER,
    tax INTEGER,
    lens_type TEXT,
    lens_design TEXT,
    lens_index TEXT,
    lens_cute TEXT,
    contactLensColorName TEXT,
    contactLens_color TEXT,
    contactLensLensmaterial TEXT,
    contactLensLensdesign TEXT,
    contactLens_type TEXT,
    framCotegery TEXT,
    framCotegeryHistory TEXT,
    serieal text Not NULL UNIQUE,
    FOREIGN KEY (brand_id) REFERENCES brand (brand_id) ON DELETE CASCADE ON UPDATE NO ACTION,
    FOREIGN KEY (company_id) REFERENCES company (company_id) ON DELETE CASCADE ON UPDATE NO ACTION,
    FOREIGN KEY (user_id) REFERENCES users (user_id) ON DELETE CASCADE ON UPDATE NO ACTION
);

CREATE TABLE ipn (
    unix INT(10),
    payment_date VARCHAR(30),
    username VARCHAR(20),
    last_name VARCHAR(30),
    payment_gross FLOAT(6, 2),
    payment_fee FLOAT(6, 2),
    payment_net FLOAT(6, 2),
    payment_status VARCHAR(15),
    txn_id VARCHAR(25)
);
CREATE TABLE users (
user_id INTEGER PRIMARY KEY,
    user_name TEXT NOT NULL,
first_name TEXT NOT NULL,
last_name TEXT NOT NULL,
email TEXT NOT NULL UNIQUE,
phone TEXT NOT NULL UNIQUE,
    hash TEXT NOT NULL UNIQUE
, U_type TEXT, wallet text DEFAULT 10000);

CREATE TABLE address  (
    address_id INTEGER NOT NULL PRIMARY KEY,
    date_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    countery_name TEXT,
    Region TEXT,
    city_name TEXT,
    district_name TEXT,
    street TEXT,
    buliding_number TEXT,
    unit_number TEXT,
    zip_code Text,
    extend_zip_code Text,
    user_id INTEGER,
    userIP Text,
    location_description Text,
    location_url Text,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE ON UPDATE NO ACTION
);



CREATE TABLE payment (
    payment_id INTEGER NOT NULL PRIMARY KEY,
    date_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    totalAmount FLOAT(6, 2),
    payment_fee FLOAT(6, 2),
    payment_net FLOAT(6, 2),
    totalQuanet INTEGER,
    paymentdatiels TEXT ,
    payment_order_id VARCHAR(25),
    payment_status VARCHAR(15),
    user_Id INTEGER,
    FOREIGN KEY (user_Id) REFERENCES users(user_id) ON DELETE CASCADE ON UPDATE NO ACTION

);



-- ALTER TABLE payment AUTO_INCREMENT = 1000
--  create table PrimaryKey1000Demo
--  (ProductId int auto_increment,
--  PRIMARY KEY(ProductId));
-- alter table PrimaryKey1000Demo AUTO_INCREMENT=1000;

--  alter table PrimaryKey1000Demo auto_increment=1000;


 
--  product table crat table order 
CREATE TABLE product(
    product_id INTEGER NOT NULL PRIMARY KEY,
    date_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    item_description TEXT,
    discount INTEGER,
    retialPrice INTEGER,
    wholePrice INTEGER,
    quant INTEGER,
    Collection_name TEXT,
    SKUCode TEXT,
    UPCcode TEXT,
    temple_length TEXT,
    lens_size TEXT,
    bridge_size TEXT,
    color TEXT,
    Model_no TEXT,
    brand_type TEXT,
    brand_id INTEGER,
    company_id INTEGER,
    user_id INTEGER,
    tax INTEGER,
    lens_type TEXT,
    lens_design TEXT,
    lens_index TEXT,
    lens_cute TEXT,
    contactLensColorName TEXT,
    contactLens_color TEXT,
    contactLensLensmaterial TEXT,
    contactLensLensdesign TEXT,
    contactLens_type TEXT,
    framCotegery TEXT,
    framCotegeryHistory TEXT,
    serieal text Not NULL UNIQUE,
    FOREIGN KEY (brand_id) REFERENCES brand (brand_id) ON DELETE CASCADE ON UPDATE NO ACTION,
    FOREIGN KEY (company_id) REFERENCES company (company_id) ON DELETE CASCADE ON UPDATE NO ACTION,
    FOREIGN KEY (user_id) REFERENCES users (user_id) ON DELETE CASCADE ON UPDATE NO ACTION
);
ALTER TABLE invoice
  ADD date_time DATETIME DEFAULT CURRENT_TIMESTAMP;
CREATE TABLE invoice (
    invoice_id INTEGER NOT NULL PRIMARY KEY ,
    date_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    totalAmount FLOAT(6, 2),
    commercial_no Text,
    totalQuanet INTEGER,
    payment_status VARCHAR(15),
    userName Text ,
    userTell Text,
    userIdNo Text,
    companyNamy Text,
    branch_name Text,
    invoiceType TEXt,
    taxValue TEXT ,
    taxAmount text,
    user_Id INTEGER,
    branch_id INTEGER,
    payment_id INTEGER,
    order_id INTEGER,
    FOREIGN KEY (order_id) REFERENCES order_trak(order_id) ON DELETE CASCADE ON UPDATE NO ACTION
    FOREIGN KEY (payment_id) REFERENCES payment(payment_id) ON DELETE CASCADE ON UPDATE NO ACTION
    FOREIGN KEY (user_Id) REFERENCES users(user_id) ON DELETE CASCADE ON UPDATE NO ACTION
    FOREIGN KEY (branch_id) REFERENCES branchs(branch_id) ON DELETE CASCADE ON UPDATE NO ACTION
);
-- insert into test values (999, 'a');
insert into invoice_datieals (invoice_datieals_id) values (0001);
CREATE TABLE invoice_datieals (
    invoice_datieals_id INTEGER NOT NULL  PRIMARY KEY ,
    iteamAmount FLOAT(6, 2),
    iteamquent FLOAT(6, 2),
    Price FLOAT(6, 2),
    discout FLOAT(6, 2),
    netPrice FLOAT(6, 2),
    productDescrptian Text,
    totalIteamsAmount text,
    product_id INTEGER,
    invoice_id INTEGER,
    FOREIGN KEY (product_id) REFERENCES producat(product_id) ON DELETE CASCADE ON UPDATE NO ACTION
    FOREIGN KEY (invoice_id) REFERENCES invoice(invoice_id) ON DELETE CASCADE ON UPDATE NO ACTION

);

        DELETE
FROM
    invoice_datieals
where
    invoice_datieals_id =1 :3



CREATE TABLE notifications (
    notifications_id INTEGER NOT NULL PRIMARY KEY,
    date_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    notes text ,
    datiles text,
    status text,
    user_id INTEGER,
    FOREIGN KEY (user_Id) REFERENCES users(user_id) ON DELETE CASCADE ON UPDATE NO ACTION


);



-- SELECT datetime('2023-03-05 10:00:00', '+2 hours'); -- Adds two hours to a time value

CREATE TABLE coustmearMessage (
    coustmearMessage_id INTEGER NOT NULL PRIMARY KEY,
    date_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    name text ,
    email text,
    tell text,
    MessageBody INTEGER,
    notes text,
    status INTEGER DEFAULT 0,
    admin_id INTEGER

);


CREATE TABLE addJops(
    jops_is INTEGER NOT NULL PRIMARY KEY,
    date_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    Title text ,
    startIn date,
    EndIn date,
    datiles INTEGER,
    requermeant text,
    sallery text,
    loctian  INTEGER DEFAULT 0,
    admin_id INTEGER
);


ALTER TABLE branchs
  ADD firstShiftOPen time DEFAULT '09:00:00';
  ADD firstShiftClose time DEFAULT '12:00:00';
  ADD secandShiftOPen time DEFAULT '05:00:00'
    ALTER TABLE branchs
  ADD secandfirstShiftClose time DEFAULT '10:30:00',
      ALTER TABLE branchs

  Add loctian text DEFAULT 'Ksa -Jeddah',
      ALTER TABLE branchs

  Add brancTell text DEFAULT 9661200000000  ;

cursor.execute(""" UPDATE invoice SET status=:status  WHERE invoice_id=:invoice_id;""",  {"status":1,'invoice_id':invoice_id})

UPDATE users SET user_id=1004 WHERE user_id=4;

UPDATE company SET company_id=2001 WHERE company_id=1001;
UPDATE brand SET company_id=2004 WHERE user_id=1004;
UPDATE brand SET user_id=1001 WHERE user_id=1;
UPDATE brand SET brand_id=4004   WHERE brand_id=4010;
UPDATE brand SET brand_id=4009   WHERE brand_id=9;

UPDATE branchs SET branch_id=3003 WHERE branch_id=1002;
UPDATE branchs SET user_id=1002 WHERE user_id=2;

UPDATE addMedia SET media_id=6001 WHERE media_id=2;
UPDATE product SET product_id=5001 WHERE product_id=1;
UPDATE product SET framCotegery='glasses' WHERE product_id=5003;

DELETE FROM product where product_id =5001  -- to deleat table

DELETE FROM  payment where payment_id =8000

UPDATE brand SET company_id=2004 WHERE brand_id=4006;
UPDATE order_trak SET order_id=9001 WHERE order_id=1;
UPDATE coustmearMessage SET coustmearMessage_id=30001 WHERE coustmearMessage_id=30000;
UPDATE addJops SET jops_is=40002 WHERE jops_is=2;


UPDATE product SET  framCotegery='Accessories' WHERE product_id=5011;

DELETE FROM product where product_id =5010;  
DELETE FROM order_trak where order_id >9001;

ALTER TABLE   product DROP contactLens_type
--  product table crat table order 
ALTER TABLE product ADD brand_type text DEFAULT 0;

insert into payment (payment_id) values (8000);
insert into notifications (notifications_id) values (20000);
insert into coustmearMessage (coustmearMessage_id) values (20000);

DELETE FROM  notifications where notifications_id =10000






18,145