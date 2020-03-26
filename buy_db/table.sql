create table companys
(
  id              INTEGER not null 
    primary key ,
  name            varchar(128) default '' not null,
  owner           varchar(256) default '' not null,
  tele            varchar(32)  default '' not null,
  detail          varchar(512) default '' not null,
  production_kind varchar(256) default '' not null,
  type            tinyint  default 0,
  created_at      TIMESTAMP    default NULL,
  updated_at      TIMESTAMP    default NULL,
  deleted_at      TIMESTAMP    default NULL,
  updated_by      VARCHAR(255) default '' not null,
  created_by      VARCHAR(255) default '' not null
);

create table kinds
(
  id         INTEGER not null
    primary key,
  name       varchar(64)  default '' not null,
  created_at TIMESTAMP    default NULL,
  updated_at TIMESTAMP    default NULL,
  deleted_at TIMESTAMP    default NULL,
  updated_by VARCHAR(255) default '' not null,
  created_by VARCHAR(255) default '' not null
);

create table results
(
  id              INTEGER not null
    primary key,
  company_id      int not null,
  kind            tinyint      default 0 not null,
  production_type varchar(32)  default '' not null,
  created_at      TIMESTAMP    default NULL,
  updated_at      TIMESTAMP    default NULL,
  deleted_at      TIMESTAMP    default NULL,
  updated_by      VARCHAR(255) default '' not null,
  created_by      VARCHAR(255) default '' not null
);

