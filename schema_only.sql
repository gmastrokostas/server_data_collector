--
-- PostgreSQL database dump
--

-- Dumped from database version 14.10
-- Dumped by pg_dump version 14.10

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
-- Name: a1servers; Type: TABLE; Schema: serverdata_schema; Owner: seeker
--

CREATE TABLE serverdata_schema.a1servers (
    serverid integer NOT NULL,
    hostname character varying(30) NOT NULL,
    date_cpt character varying(10),
    time_cpt character varying(10),
    os character varying(20),
    osrel character varying(5),
    selinux_status character varying(10),
    selinux_mode character varying(10),
    selinux_type character varying(10),
    total_m bigint,
    cpubrand character varying(100),
    cores integer,
    arch character varying(10),
    server_brand character varying(100),
    virt_role character varying(10),
    virt_type character varying(10),
    uptime integer
);


ALTER TABLE serverdata_schema.a1servers OWNER TO seeker;

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
-- Name: external_routes; Type: TABLE; Schema: serverdata_schema; Owner: seeker
--

CREATE TABLE serverdata_schema.external_routes (
    route_name character varying(50) NOT NULL,
    route_ip character varying(50) NOT NULL
);


ALTER TABLE serverdata_schema.external_routes OWNER TO seeker;

--
-- Name: hpv_vm_inventory; Type: TABLE; Schema: serverdata_schema; Owner: seeker
--

CREATE TABLE serverdata_schema.hpv_vm_inventory (
    serverid integer,
    hostname character varying(50),
    vmname character varying(30),
    date_cpt character varying(10),
    time_cpt character varying(10)
);


ALTER TABLE serverdata_schema.hpv_vm_inventory OWNER TO seeker;

--
-- Name: internal_routes; Type: TABLE; Schema: serverdata_schema; Owner: seeker
--

CREATE TABLE serverdata_schema.internal_routes (
    route_name character varying(50) NOT NULL,
    route_ip character varying(50) NOT NULL
);


ALTER TABLE serverdata_schema.internal_routes OWNER TO seeker;

--
-- Name: lvm_setup; Type: TABLE; Schema: serverdata_schema; Owner: seeker
--

CREATE TABLE serverdata_schema.lvm_setup (
    serverid integer,
    hostname character varying(50),
    pvs_info character varying(100),
    vgs_info character varying(100),
    lvs_info character varying(100),
    dev_mapper character varying(100)
);


ALTER TABLE serverdata_schema.lvm_setup OWNER TO seeker;

--
-- Name: network_interfaces; Type: TABLE; Schema: serverdata_schema; Owner: seeker
--

CREATE TABLE serverdata_schema.network_interfaces (
    serverid integer,
    hostname character varying(50),
    ifname character varying(50),
    ipaddr character varying(30),
    netmask character varying(30)
);


ALTER TABLE serverdata_schema.network_interfaces OWNER TO seeker;

--
-- Name: network_routes; Type: TABLE; Schema: serverdata_schema; Owner: seeker
--

CREATE TABLE serverdata_schema.network_routes (
    serverid integer,
    hostname character varying(50),
    ifname character varying(50),
    destn character varying(30),
    gateway character varying(30),
    netmsk character varying(30)
);


ALTER TABLE serverdata_schema.network_routes OWNER TO seeker;

--
-- Name: network_setup; Type: TABLE; Schema: serverdata_schema; Owner: seeker
--

CREATE TABLE serverdata_schema.network_setup (
    serverid integer,
    hostname character varying(50),
    default_interface character varying(10),
    default_route inet,
    interface_type character varying(10),
    dns_entries character varying(200),
    date_cpt character varying(10),
    time_cpt character varying(10)
);


ALTER TABLE serverdata_schema.network_setup OWNER TO seeker;

--
-- Name: rpm_packages; Type: TABLE; Schema: serverdata_schema; Owner: seeker
--

CREATE TABLE serverdata_schema.rpm_packages (
    serverid integer,
    hostname character varying(50),
    date_cpt character varying(10),
    time_cpt character varying(10),
    rpm_name character varying(200),
    rpm_version character varying(200),
    rpm_release character varying(100)
);


ALTER TABLE serverdata_schema.rpm_packages OWNER TO seeker;

--
-- Name: sar_cpu_perf; Type: TABLE; Schema: serverdata_schema; Owner: seeker
--

CREATE TABLE serverdata_schema.sar_cpu_perf (
    hostname character varying(30) NOT NULL,
    "interval" integer NOT NULL,
    "timestamp" timestamp with time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    cpu smallint NOT NULL,
    pct_user numeric(5,2) NOT NULL,
    pct_nice numeric(5,2) NOT NULL,
    pct_systm numeric(5,2) NOT NULL,
    pct_iowait numeric(5,2) NOT NULL,
    pct_steal numeric(5,2) NOT NULL,
    pct_idle numeric(5,2) NOT NULL
);


ALTER TABLE serverdata_schema.sar_cpu_perf OWNER TO seeker;

--
-- Name: sar_disk_perf; Type: TABLE; Schema: serverdata_schema; Owner: seeker
--

CREATE TABLE serverdata_schema.sar_disk_perf (
    hostname character varying(30) NOT NULL,
    "interval" integer NOT NULL,
    "timestamp" timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
    dev character varying(100) NOT NULL,
    tps numeric(9,2) NOT NULL,
    rkbs numeric(9,2) NOT NULL,
    wkbs numeric(9,2) NOT NULL,
    areq_sz numeric(9,2) NOT NULL,
    aqu_sz numeric(9,2) NOT NULL,
    await numeric(9,2) NOT NULL,
    svctm numeric(9,2) NOT NULL,
    pct_utilzed numeric(5,2) NOT NULL
);


ALTER TABLE serverdata_schema.sar_disk_perf OWNER TO seeker;

--
-- Name: sar_errors_net_perf; Type: TABLE; Schema: serverdata_schema; Owner: seeker
--

CREATE TABLE serverdata_schema.sar_errors_net_perf (
    hostname character varying(30) NOT NULL,
    "interval" integer NOT NULL,
    "timestamp" timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
    iface character varying(128) NOT NULL,
    rxerrs numeric(9,2) NOT NULL,
    txerrs numeric(9,2) NOT NULL,
    colls numeric(9,2) NOT NULL,
    rxdrop numeric(9,2) NOT NULL,
    txdrop numeric(9,2) NOT NULL,
    txcarr numeric(9,2) NOT NULL,
    rxfram numeric(9,2) NOT NULL,
    rxfifo numeric(9,2) NOT NULL,
    txfifo numeric(9,2) NOT NULL
);


ALTER TABLE serverdata_schema.sar_errors_net_perf OWNER TO seeker;

--
-- Name: sar_mem_perf; Type: TABLE; Schema: serverdata_schema; Owner: seeker
--

CREATE TABLE serverdata_schema.sar_mem_perf (
    hostname character varying(30) NOT NULL,
    "interval" integer NOT NULL,
    "timestamp" timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
    kbmemfree integer NOT NULL,
    kbavail integer NOT NULL,
    kbmemused integer NOT NULL,
    pct_memused numeric(5,2) NOT NULL,
    kbbuffers integer NOT NULL,
    kbcached integer NOT NULL,
    kbcommit integer NOT NULL,
    pct_commit numeric(5,2) NOT NULL,
    kbactive integer NOT NULL,
    kbinact integer NOT NULL,
    kbdirty integer NOT NULL
);


ALTER TABLE serverdata_schema.sar_mem_perf OWNER TO seeker;

--
-- Name: sar_net_perf; Type: TABLE; Schema: serverdata_schema; Owner: seeker
--

CREATE TABLE serverdata_schema.sar_net_perf (
    hostname character varying(30) NOT NULL,
    "interval" integer NOT NULL,
    "timestamp" timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
    iface character varying(128) NOT NULL,
    rxpcks numeric(9,2) NOT NULL,
    txpcks numeric(9,2) NOT NULL,
    rxkbs numeric(9,2) NOT NULL,
    txkbs numeric(9,2) NOT NULL,
    rxcmps numeric(9,2) NOT NULL,
    txcmps numeric(9,2) NOT NULL,
    rxxcsts numeric(9,2) NOT NULL,
    pct_utilzed numeric(5,2) NOT NULL
);


ALTER TABLE serverdata_schema.sar_net_perf OWNER TO seeker;

--
-- Name: sar_page_perf; Type: TABLE; Schema: serverdata_schema; Owner: seeker
--

CREATE TABLE serverdata_schema.sar_page_perf (
    hostname character varying(128) NOT NULL,
    "interval" integer NOT NULL,
    "timestamp" timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
    pgins numeric(9,2) NOT NULL,
    pgouts numeric(9,2) NOT NULL,
    faults numeric(9,2) NOT NULL,
    mfaults numeric(9,2) NOT NULL,
    pgfrees numeric(9,2) NOT NULL,
    pgscanks numeric(9,2) NOT NULL,
    pgscands numeric(9,2) NOT NULL,
    pgsteals numeric(9,2) NOT NULL,
    pct_vmeff numeric(5,2) NOT NULL
);


ALTER TABLE serverdata_schema.sar_page_perf OWNER TO seeker;

--
-- Name: storage_capacity; Type: TABLE; Schema: serverdata_schema; Owner: seeker
--

CREATE TABLE serverdata_schema.storage_capacity (
    serverid integer,
    hostname character varying(50),
    mount character varying(150),
    fstype character varying(10),
    device character varying(50),
    size_available bigint,
    size_total bigint,
    size_available_human character varying(20),
    size_total_human character varying(20),
    moption character varying(300),
    uuid character varying(100),
    date_cpt character varying(10),
    time_cpt character varying(10)
);


ALTER TABLE serverdata_schema.storage_capacity OWNER TO seeker;

--
-- Name: view_interface_gateways; Type: VIEW; Schema: serverdata_schema; Owner: seeker
--

CREATE VIEW serverdata_schema.view_interface_gateways AS
 SELECT DISTINCT a1servers.hostname,
    network_routes.gateway,
    network_interfaces.ifname
   FROM ((serverdata_schema.network_interfaces
     JOIN serverdata_schema.network_routes ON (((network_interfaces.ifname)::text = (network_routes.ifname)::text)))
     JOIN serverdata_schema.a1servers ON (((a1servers.hostname)::text = (network_interfaces.hostname)::text)))
  ORDER BY a1servers.hostname;


ALTER TABLE serverdata_schema.view_interface_gateways OWNER TO seeker;

--
-- Name: view_lvm_setup; Type: VIEW; Schema: serverdata_schema; Owner: seeker
--

CREATE VIEW serverdata_schema.view_lvm_setup AS
 SELECT a1servers.serverid,
    a1servers.hostname,
    storage_capacity.mount,
    storage_capacity.fstype,
    lvm_setup.pvs_info,
    lvm_setup.vgs_info,
    lvm_setup.lvs_info,
    storage_capacity.device,
    storage_capacity.size_available,
    storage_capacity.size_available_human,
    storage_capacity.size_total,
    storage_capacity.size_total_human
   FROM ((serverdata_schema.storage_capacity
     JOIN serverdata_schema.a1servers ON ((a1servers.serverid = storage_capacity.serverid)))
     JOIN serverdata_schema.lvm_setup ON (((storage_capacity.device)::text = (lvm_setup.dev_mapper)::text)));


ALTER TABLE serverdata_schema.view_lvm_setup OWNER TO seeker;

--
-- Name: external_routes pk_external_routes; Type: CONSTRAINT; Schema: serverdata_schema; Owner: seeker
--

ALTER TABLE ONLY serverdata_schema.external_routes
    ADD CONSTRAINT pk_external_routes PRIMARY KEY (route_name, route_ip);


--
-- Name: internal_routes pk_internal_routes; Type: CONSTRAINT; Schema: serverdata_schema; Owner: seeker
--

ALTER TABLE ONLY serverdata_schema.internal_routes
    ADD CONSTRAINT pk_internal_routes PRIMARY KEY (route_name, route_ip);


--
-- Name: a1servers pk_servers_integer; Type: CONSTRAINT; Schema: serverdata_schema; Owner: seeker
--

ALTER TABLE ONLY serverdata_schema.a1servers
    ADD CONSTRAINT pk_servers_integer PRIMARY KEY (serverid);


--
-- Name: command_line_options fk_command_line_options; Type: FK CONSTRAINT; Schema: serverdata_schema; Owner: seeker
--

ALTER TABLE ONLY serverdata_schema.command_line_options
    ADD CONSTRAINT fk_command_line_options FOREIGN KEY (serverid) REFERENCES serverdata_schema.a1servers(serverid) MATCH FULL;


--
-- Name: hpv_vm_inventory fk_hpv_vm_inventory; Type: FK CONSTRAINT; Schema: serverdata_schema; Owner: seeker
--

ALTER TABLE ONLY serverdata_schema.hpv_vm_inventory
    ADD CONSTRAINT fk_hpv_vm_inventory FOREIGN KEY (serverid) REFERENCES serverdata_schema.a1servers(serverid) MATCH FULL;


--
-- Name: network_interfaces fk_network_interface; Type: FK CONSTRAINT; Schema: serverdata_schema; Owner: seeker
--

ALTER TABLE ONLY serverdata_schema.network_interfaces
    ADD CONSTRAINT fk_network_interface FOREIGN KEY (serverid) REFERENCES serverdata_schema.a1servers(serverid) MATCH FULL;


--
-- Name: network_routes fk_network_routes; Type: FK CONSTRAINT; Schema: serverdata_schema; Owner: seeker
--

ALTER TABLE ONLY serverdata_schema.network_routes
    ADD CONSTRAINT fk_network_routes FOREIGN KEY (serverid) REFERENCES serverdata_schema.a1servers(serverid) MATCH FULL;


--
-- Name: network_setup fk_network_setup; Type: FK CONSTRAINT; Schema: serverdata_schema; Owner: seeker
--

ALTER TABLE ONLY serverdata_schema.network_setup
    ADD CONSTRAINT fk_network_setup FOREIGN KEY (serverid) REFERENCES serverdata_schema.a1servers(serverid) MATCH FULL;


--
-- Name: rpm_packages fk_rpm_packages; Type: FK CONSTRAINT; Schema: serverdata_schema; Owner: seeker
--

ALTER TABLE ONLY serverdata_schema.rpm_packages
    ADD CONSTRAINT fk_rpm_packages FOREIGN KEY (serverid) REFERENCES serverdata_schema.a1servers(serverid) MATCH FULL;


--
-- Name: storage_capacity storage_capacity_fk; Type: FK CONSTRAINT; Schema: serverdata_schema; Owner: seeker
--

ALTER TABLE ONLY serverdata_schema.storage_capacity
    ADD CONSTRAINT storage_capacity_fk FOREIGN KEY (serverid) REFERENCES serverdata_schema.a1servers(serverid) MATCH FULL;


--
-- Name: lvm_setup storage_setup_fk; Type: FK CONSTRAINT; Schema: serverdata_schema; Owner: seeker
--

ALTER TABLE ONLY serverdata_schema.lvm_setup
    ADD CONSTRAINT storage_setup_fk FOREIGN KEY (serverid) REFERENCES serverdata_schema.a1servers(serverid) MATCH FULL;


--
-- Name: SCHEMA serverdata_schema; Type: ACL; Schema: -; Owner: seeker
--

GRANT USAGE ON SCHEMA serverdata_schema TO ro_seeker;


--
-- Name: TABLE a1servers; Type: ACL; Schema: serverdata_schema; Owner: seeker
--

GRANT SELECT ON TABLE serverdata_schema.a1servers TO ro_seeker;


--
-- Name: TABLE command_line_options; Type: ACL; Schema: serverdata_schema; Owner: seeker
--

GRANT SELECT ON TABLE serverdata_schema.command_line_options TO ro_seeker;


--
-- Name: TABLE external_routes; Type: ACL; Schema: serverdata_schema; Owner: seeker
--

GRANT SELECT ON TABLE serverdata_schema.external_routes TO ro_seeker;


--
-- Name: TABLE hpv_vm_inventory; Type: ACL; Schema: serverdata_schema; Owner: seeker
--

GRANT SELECT ON TABLE serverdata_schema.hpv_vm_inventory TO ro_seeker;


--
-- Name: TABLE internal_routes; Type: ACL; Schema: serverdata_schema; Owner: seeker
--

GRANT SELECT ON TABLE serverdata_schema.internal_routes TO ro_seeker;


--
-- Name: TABLE lvm_setup; Type: ACL; Schema: serverdata_schema; Owner: seeker
--

GRANT SELECT ON TABLE serverdata_schema.lvm_setup TO ro_seeker;


--
-- Name: TABLE network_interfaces; Type: ACL; Schema: serverdata_schema; Owner: seeker
--

GRANT SELECT ON TABLE serverdata_schema.network_interfaces TO ro_seeker;


--
-- Name: TABLE network_routes; Type: ACL; Schema: serverdata_schema; Owner: seeker
--

GRANT SELECT ON TABLE serverdata_schema.network_routes TO ro_seeker;


--
-- Name: TABLE network_setup; Type: ACL; Schema: serverdata_schema; Owner: seeker
--

GRANT SELECT ON TABLE serverdata_schema.network_setup TO ro_seeker;


--
-- Name: TABLE rpm_packages; Type: ACL; Schema: serverdata_schema; Owner: seeker
--

GRANT SELECT ON TABLE serverdata_schema.rpm_packages TO ro_seeker;


--
-- Name: TABLE sar_cpu_perf; Type: ACL; Schema: serverdata_schema; Owner: seeker
--

GRANT SELECT ON TABLE serverdata_schema.sar_cpu_perf TO ro_seeker;


--
-- Name: TABLE sar_disk_perf; Type: ACL; Schema: serverdata_schema; Owner: seeker
--

GRANT SELECT ON TABLE serverdata_schema.sar_disk_perf TO ro_seeker;


--
-- Name: TABLE sar_errors_net_perf; Type: ACL; Schema: serverdata_schema; Owner: seeker
--

GRANT SELECT ON TABLE serverdata_schema.sar_errors_net_perf TO ro_seeker;


--
-- Name: TABLE sar_mem_perf; Type: ACL; Schema: serverdata_schema; Owner: seeker
--

GRANT SELECT ON TABLE serverdata_schema.sar_mem_perf TO ro_seeker;


--
-- Name: TABLE sar_net_perf; Type: ACL; Schema: serverdata_schema; Owner: seeker
--

GRANT SELECT ON TABLE serverdata_schema.sar_net_perf TO ro_seeker;


--
-- Name: TABLE sar_page_perf; Type: ACL; Schema: serverdata_schema; Owner: seeker
--

GRANT SELECT ON TABLE serverdata_schema.sar_page_perf TO ro_seeker;


--
-- Name: TABLE storage_capacity; Type: ACL; Schema: serverdata_schema; Owner: seeker
--

GRANT SELECT ON TABLE serverdata_schema.storage_capacity TO ro_seeker;


--
-- Name: TABLE view_interface_gateways; Type: ACL; Schema: serverdata_schema; Owner: seeker
--

GRANT SELECT ON TABLE serverdata_schema.view_interface_gateways TO ro_seeker;


--
-- Name: TABLE view_lvm_setup; Type: ACL; Schema: serverdata_schema; Owner: seeker
--

GRANT SELECT ON TABLE serverdata_schema.view_lvm_setup TO ro_seeker;


--
-- Name: DEFAULT PRIVILEGES FOR TABLES; Type: DEFAULT ACL; Schema: serverdata_schema; Owner: seeker
--

ALTER DEFAULT PRIVILEGES FOR ROLE seeker IN SCHEMA serverdata_schema GRANT SELECT ON TABLES  TO ro_seeker;


--
-- PostgreSQL database dump complete
--

