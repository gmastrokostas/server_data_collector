--
-- PostgreSQL database dump
--

-- Dumped from database version 14.1
-- Dumped by pg_dump version 14.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: serverdata; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE serverdata WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'en_US.UTF-8';


ALTER DATABASE serverdata OWNER TO postgres;

\connect serverdata

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: serverdata; Type: DATABASE PROPERTIES; Schema: -; Owner: postgres
--

ALTER DATABASE serverdata SET search_path TO 'pico_schema';


\connect serverdata

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: pico_schema; Type: SCHEMA; Schema: -; Owner: seeker
--

CREATE SCHEMA pico_schema;


ALTER SCHEMA pico_schema OWNER TO seeker;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: hpv_vm_inventory; Type: TABLE; Schema: pico_schema; Owner: seeker
--

CREATE TABLE pico_schema.hpv_vm_inventory (
    hostname text,
    vmname text,
    date_cpt text,
    time_cpt text
);


ALTER TABLE pico_schema.hpv_vm_inventory OWNER TO seeker;

--
-- Name: network_setup; Type: TABLE; Schema: pico_schema; Owner: seeker
--

CREATE TABLE pico_schema.network_setup (
    hostname text,
    default_interface text,
    default_route inet,
    interface_type text,
    dns_entries text,
    date_cpt text,
    time_cpt text
);


ALTER TABLE pico_schema.network_setup OWNER TO seeker;

--
-- Name: rpm_packages; Type: TABLE; Schema: pico_schema; Owner: seeker
--

CREATE TABLE pico_schema.rpm_packages (
    hostname text,
    date_cpt text,
    time_cpt text,
    rpm_name text,
    rpm_version text,
    rpm_release text
);


ALTER TABLE pico_schema.rpm_packages OWNER TO seeker;

--
-- Name: rpm_packages_pre; Type: TABLE; Schema: pico_schema; Owner: seeker
--

CREATE TABLE pico_schema.rpm_packages_pre (
    hostname text,
    date_cpt text,
    time_cpt text,
    rpm_name text,
    rpm_version text,
    rpm_release text
);


ALTER TABLE pico_schema.rpm_packages_pre OWNER TO seeker;

--
-- Name: servers; Type: TABLE; Schema: pico_schema; Owner: seeker
--

CREATE TABLE pico_schema.servers (
    hostname text NOT NULL,
    date_cpt text,
    time_cpt text,
    os text,
    osrel text,
    total_m text,
    cpubrand text,
    cores text,
    arch text,
    server_brand text,
    virt_role text,
    virt_type text,
    uptime text
);


ALTER TABLE pico_schema.servers OWNER TO seeker;

--
-- Name: storage_setup; Type: TABLE; Schema: pico_schema; Owner: seeker
--

CREATE TABLE pico_schema.storage_setup (
    hostname character varying(50),
    mount character varying(10),
    fstype character varying(10),
    device character varying(50),
    moption character varying(100),
    uuid character varying(100),
    swap_mount character varying(50),
    swap_total_mb integer,
    swap_free integer,
    date_cpt text,
    time_cpt text
);


ALTER TABLE pico_schema.storage_setup OWNER TO seeker;

--
-- Name: servers pk_servers_hostname; Type: CONSTRAINT; Schema: pico_schema; Owner: seeker
--

ALTER TABLE ONLY pico_schema.servers
    ADD CONSTRAINT pk_servers_hostname PRIMARY KEY (hostname);


--
-- Name: network_setup fk_network_setup_hostname; Type: FK CONSTRAINT; Schema: pico_schema; Owner: seeker
--

ALTER TABLE ONLY pico_schema.network_setup
    ADD CONSTRAINT fk_network_setup_hostname FOREIGN KEY (hostname) REFERENCES pico_schema.servers(hostname) ON DELETE CASCADE;


--
-- Name: rpm_packages fk_rpms_pckgs_hostname; Type: FK CONSTRAINT; Schema: pico_schema; Owner: seeker
--

ALTER TABLE ONLY pico_schema.rpm_packages
    ADD CONSTRAINT fk_rpms_pckgs_hostname FOREIGN KEY (hostname) REFERENCES pico_schema.servers(hostname) ON DELETE CASCADE;


--
-- Name: rpm_packages_pre fk_rpms_pckgs_hostname; Type: FK CONSTRAINT; Schema: pico_schema; Owner: seeker
--

ALTER TABLE ONLY pico_schema.rpm_packages_pre
    ADD CONSTRAINT fk_rpms_pckgs_hostname FOREIGN KEY (hostname) REFERENCES pico_schema.servers(hostname) ON DELETE CASCADE;


--
-- Name: hpv_vm_inventory fk_vminventory; Type: FK CONSTRAINT; Schema: pico_schema; Owner: seeker
--

ALTER TABLE ONLY pico_schema.hpv_vm_inventory
    ADD CONSTRAINT fk_vminventory FOREIGN KEY (hostname) REFERENCES pico_schema.servers(hostname) ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

