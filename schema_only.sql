--
-- PostgreSQL database dump
--

-- Dumped from database version 14.4
-- Dumped by pg_dump version 14.4

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
-- Name: serverdata_schema; Type: SCHEMA; Schema: -; Owner: seeker
--

CREATE SCHEMA serverdata_schema;


ALTER SCHEMA serverdata_schema OWNER TO seeker;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: command_line_options; Type: TABLE; Schema: serverdata_schema; Owner: seeker
--

CREATE TABLE serverdata_schema.command_line_options (
    serverid integer,
    hostname character varying(50),
    cmnd_options character varying(200)
);


ALTER TABLE serverdata_schema.command_line_options OWNER TO seeker;

--
-- Name: hpv_vm_inventory; Type: TABLE; Schema: serverdata_schema; Owner: seeker
--

CREATE TABLE serverdata_schema.hpv_vm_inventory (
    serverid integer,
    hostname character varying(30),
    vmname character varying(30),
    date_cpt character varying(10),
    time_cpt character varying(10)
);


ALTER TABLE serverdata_schema.hpv_vm_inventory OWNER TO seeker;

--
-- Name: network_setup; Type: TABLE; Schema: serverdata_schema; Owner: seeker
--

CREATE TABLE serverdata_schema.network_setup (
    serverid integer,
    hostname character varying(30),
    default_interface character varying(10),
    default_route inet,
    interface_type character varying(10),
    dns_entries character varying(100),
    date_cpt character varying(10),
    time_cpt character varying(10)
);


ALTER TABLE serverdata_schema.network_setup OWNER TO seeker;

--
-- Name: rpm_packages; Type: TABLE; Schema: serverdata_schema; Owner: seeker
--

CREATE TABLE serverdata_schema.rpm_packages (
    serverid integer,
    hostname character varying(30),
    date_cpt character varying(10),
    time_cpt character varying(10),
    rpm_name character varying(200),
    rpm_version character varying(200),
    rpm_release character varying(100)
);


ALTER TABLE serverdata_schema.rpm_packages OWNER TO seeker;

--
-- Name: rpm_packages_pre; Type: TABLE; Schema: serverdata_schema; Owner: seeker
--

CREATE TABLE serverdata_schema.rpm_packages_pre (
    serverid integer,
    hostname character varying(30),
    date_cpt character varying(10),
    time_cpt character varying(10),
    rpm_name character varying,
    rpm_version character varying,
    rpm_release character varying
);


ALTER TABLE serverdata_schema.rpm_packages_pre OWNER TO seeker;

--
-- Name: servers; Type: TABLE; Schema: serverdata_schema; Owner: seeker
--

CREATE TABLE serverdata_schema.servers (
    serverid integer,
    hostname character varying(30) NOT NULL,
    date_cpt character varying(10),
    time_cpt character varying(10),
    os character varying(20),
    osrel character varying(5),
    selinux_status character varying,
    selinux_mode character varying,
    selinux_type character varying,
    total_m bigint,
    cpubrand character varying(100),
    cores integer,
    arch character varying(10),
    server_brand character varying(100),
    virt_role character varying(10),
    virt_type character varying(10),
    uptime integer
);


ALTER TABLE serverdata_schema.servers OWNER TO seeker;

--
-- Name: storage_capacity; Type: TABLE; Schema: serverdata_schema; Owner: seeker
--

CREATE TABLE serverdata_schema.storage_capacity (
    serverid integer,
    hostname character varying(50),
    mount character varying(50),
    fstype character varying(10),
    device character varying(50),
    block_available bigint,
    block_total bigint,
    block_used bigint,
    moption character varying(100),
    uuid character varying(100),
    swap_mount character varying(50),
    swap_total_mb integer,
    swap_free integer,
    date_cpt character varying(10),
    time_cpt character varying(10)
);


ALTER TABLE serverdata_schema.storage_capacity OWNER TO seeker;

--
-- Name: testing_pk; Type: TABLE; Schema: serverdata_schema; Owner: seeker
--

CREATE TABLE serverdata_schema.testing_pk (
    id integer NOT NULL,
    hostname character varying(30),
    ansible_error integer,
    platrep_error integer,
    postcheck_error integer
);


ALTER TABLE serverdata_schema.testing_pk OWNER TO seeker;

--
-- Name: testing_pk_id_seq; Type: SEQUENCE; Schema: serverdata_schema; Owner: seeker
--

CREATE SEQUENCE serverdata_schema.testing_pk_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE serverdata_schema.testing_pk_id_seq OWNER TO seeker;

--
-- Name: testing_pk_id_seq; Type: SEQUENCE OWNED BY; Schema: serverdata_schema; Owner: seeker
--

ALTER SEQUENCE serverdata_schema.testing_pk_id_seq OWNED BY serverdata_schema.testing_pk.id;


--
-- Name: testing_pk id; Type: DEFAULT; Schema: serverdata_schema; Owner: seeker
--

ALTER TABLE ONLY serverdata_schema.testing_pk ALTER COLUMN id SET DEFAULT nextval('serverdata_schema.testing_pk_id_seq'::regclass);


--
-- Name: servers pk_servers_hostname; Type: CONSTRAINT; Schema: serverdata_schema; Owner: seeker
--

ALTER TABLE ONLY serverdata_schema.servers
    ADD CONSTRAINT pk_servers_hostname PRIMARY KEY (hostname);


--
-- Name: testing_pk testing_pk_pkey; Type: CONSTRAINT; Schema: serverdata_schema; Owner: seeker
--

ALTER TABLE ONLY serverdata_schema.testing_pk
    ADD CONSTRAINT testing_pk_pkey PRIMARY KEY (id);


--
-- Name: command_line_options command_line_options_fk; Type: FK CONSTRAINT; Schema: serverdata_schema; Owner: seeker
--

ALTER TABLE ONLY serverdata_schema.command_line_options
    ADD CONSTRAINT command_line_options_fk FOREIGN KEY (hostname) REFERENCES serverdata_schema.servers(hostname) MATCH FULL;


--
-- Name: hpv_vm_inventory hpv_vm_inventory_fk; Type: FK CONSTRAINT; Schema: serverdata_schema; Owner: seeker
--

ALTER TABLE ONLY serverdata_schema.hpv_vm_inventory
    ADD CONSTRAINT hpv_vm_inventory_fk FOREIGN KEY (hostname) REFERENCES serverdata_schema.servers(hostname) MATCH FULL;


--
-- Name: network_setup network_setup_fk; Type: FK CONSTRAINT; Schema: serverdata_schema; Owner: seeker
--

ALTER TABLE ONLY serverdata_schema.network_setup
    ADD CONSTRAINT network_setup_fk FOREIGN KEY (hostname) REFERENCES serverdata_schema.servers(hostname) MATCH FULL;


--
-- Name: rpm_packages rpm_packages_fk; Type: FK CONSTRAINT; Schema: serverdata_schema; Owner: seeker
--

ALTER TABLE ONLY serverdata_schema.rpm_packages
    ADD CONSTRAINT rpm_packages_fk FOREIGN KEY (hostname) REFERENCES serverdata_schema.servers(hostname) MATCH FULL;


--
-- Name: storage_capacity storage_capacity_fk; Type: FK CONSTRAINT; Schema: serverdata_schema; Owner: seeker
--

ALTER TABLE ONLY serverdata_schema.storage_capacity
    ADD CONSTRAINT storage_capacity_fk FOREIGN KEY (hostname) REFERENCES serverdata_schema.servers(hostname) MATCH FULL;


--
-- Name: SCHEMA serverdata_schema; Type: ACL; Schema: -; Owner: seeker
--

GRANT USAGE ON SCHEMA serverdata_schema TO ro_seeker;


--
-- Name: TABLE command_line_options; Type: ACL; Schema: serverdata_schema; Owner: seeker
--

GRANT SELECT ON TABLE serverdata_schema.command_line_options TO ro_seeker;


--
-- Name: TABLE hpv_vm_inventory; Type: ACL; Schema: serverdata_schema; Owner: seeker
--

GRANT SELECT ON TABLE serverdata_schema.hpv_vm_inventory TO ro_seeker;


--
-- Name: TABLE network_setup; Type: ACL; Schema: serverdata_schema; Owner: seeker
--

GRANT SELECT ON TABLE serverdata_schema.network_setup TO ro_seeker;


--
-- Name: TABLE rpm_packages; Type: ACL; Schema: serverdata_schema; Owner: seeker
--

GRANT SELECT ON TABLE serverdata_schema.rpm_packages TO ro_seeker;


--
-- Name: TABLE rpm_packages_pre; Type: ACL; Schema: serverdata_schema; Owner: seeker
--

GRANT SELECT ON TABLE serverdata_schema.rpm_packages_pre TO ro_seeker;


--
-- Name: TABLE servers; Type: ACL; Schema: serverdata_schema; Owner: seeker
--

GRANT SELECT ON TABLE serverdata_schema.servers TO ro_seeker;


--
-- Name: TABLE storage_capacity; Type: ACL; Schema: serverdata_schema; Owner: seeker
--

GRANT SELECT ON TABLE serverdata_schema.storage_capacity TO ro_seeker;


--
-- Name: TABLE testing_pk; Type: ACL; Schema: serverdata_schema; Owner: seeker
--

GRANT SELECT ON TABLE serverdata_schema.testing_pk TO ro_seeker;


--
-- Name: DEFAULT PRIVILEGES FOR TABLES; Type: DEFAULT ACL; Schema: serverdata_schema; Owner: seeker
--

ALTER DEFAULT PRIVILEGES FOR ROLE seeker IN SCHEMA serverdata_schema GRANT SELECT ON TABLES  TO ro_seeker;


--
-- PostgreSQL database dump complete
--

