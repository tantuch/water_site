BEGIN;

CREATE TABLE "contacts" (
	"id" INTEGER NOT NULL PRIMARY KEY,
	"address" TEXT,
	"email" TEXT,
	"telephones" TEXT
);

CREATE TABLE "products" (
	"id" INTEGER NOT NULL PRIMARY KEY,
	"name" TEXT,
	"price" REAL,
	"status" NUMERIC,
	"img_url" TEXT
);

CREATE TABLE "sertify" (
	"id" INTEGER NOT NULL PRIMARY KEY,
	"content" TEXT,
	"img_url" TEXT
);

CREATE TABLE "company" (
	"id" INTEGER NOT NULL PRIMARY KEY,
	"content" TEXT
);

COMMIT;
