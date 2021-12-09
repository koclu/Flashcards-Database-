CREATE TABLE "public.Users" (
	"user_name" serial(255) NOT NULL,
	"password" VARCHAR(255) NOT NULL,
	"total_time" integer NOT NULL,
	"current_level" integer NOT NULL,
	CONSTRAINT "Users_pk" PRIMARY KEY ("user_name")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.Words" (
	"words_id" serial NOT NULL,
	"frequency" integer,
	"Dutch" VARCHAR(255) NOT NULL,
	"English" VARCHAR(255) NOT NULL,
	"words_of_level" integer NOT NULL,
	CONSTRAINT "Words_pk" PRIMARY KEY ("words_id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.custom_levels" (
	"user_name" VARCHAR(255) NOT NULL,
	"level_name" VARCHAR(255) NOT NULL,
	"Dutch" VARCHAR(255) NOT NULL,
	"English" VARCHAR(255) NOT NULL
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.Statistics" (
	"user_name" VARCHAR(255) NOT NULL,
	"completed_level" integer NOT NULL,
	"attemps" integer NOT NULL,
	"knows" integer NOT NULL
) WITH (
  OIDS=FALSE
);





ALTER TABLE "custom_levels" ADD CONSTRAINT "custom_levels_fk0" FOREIGN KEY ("user_name") REFERENCES "Users"("user_name");

ALTER TABLE "Statistics" ADD CONSTRAINT "Statistics_fk0" FOREIGN KEY ("user_name") REFERENCES "Users"("user_name");





