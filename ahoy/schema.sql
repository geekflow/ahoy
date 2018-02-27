DROP TABLE IF EXISTS gs_version;
CREATE TABLE gs_version (
  id         INTEGER PRIMARY KEY AUTOINCREMENT,
  version    string NOT NULL,
  start_date DATETIME NOT NULL,
  end_date DATETIME NOT NULL
);

DROP TABLE IF EXISTS gs_view;
CREATE TABLE gs_view (
  id        INTEGER PRIMARY KEY AUTOINCREMENT,
  name      string NOT NULL,
  parent_id INTEGER,
  depth     INTEGER,
  sequence  INTEGER
);

DROP TABLE IF EXISTS gs_related_version_view;
CREATE TABLE gs_related_version_view (
  version_id INTEGER,
  view_id    INTEGER
);

DROP TABLE IF EXISTS gs_function;
CREATE TABLE gs_function (
  id   INTEGER PRIMARY KEY AUTOINCREMENT,
  name string NOT NULL
);

DROP TABLE IF EXISTS gs_related_view_function;
CREATE TABLE gs_related_view_function (
  version_id  INTEGER,
  view_id     INTEGER,
  function_id INTEGER
);

DROP TABLE IF EXISTS gs_condition;
CREATE TABLE gs_condition (
  id       INTEGER PRIMARY KEY AUTOINCREMENT,
  name     string NOT NULL,
  content  TEXT   NOT NULL,
  expect   TEXT   NOT NULL,
  actual   TEXT   NOT NULL,
  status   INTEGER,
  priority INTEGER,
  note     TEXT   NOT NULL
);

DROP TABLE IF EXISTS gs_related_function_condition;
CREATE TABLE gs_related_function_condition (
  version_id   INTEGER,
  function_id  INTEGER,
  condition_id INTEGER
);

DROP TABLE IF EXISTS gs_script;
CREATE TABLE gs_script (
  id      INTEGER PRIMARY KEY AUTOINCREMENT,
  content TEXT NOT NULL
);

DROP TABLE IF EXISTS gs_related_condition_script;
CREATE TABLE gs_related_function_condition (
  version_id   INTEGER,
  condition_id INTEGER,
  script_id    INTEGER
);
