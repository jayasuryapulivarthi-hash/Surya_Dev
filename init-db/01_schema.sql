--
-- PostgreSQL database dump
--

\restrict OYLdlBj3GQk2ivxrqaBytnL96Qvq5rh7ROGLyMOsX37nyJUzDDxLhU6rpHqZV3R

-- Dumped from database version 17.10
-- Dumped by pg_dump version 17.10

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: academics; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA academics;


ALTER SCHEMA academics OWNER TO postgres;

--
-- Name: student; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA student;


ALTER SCHEMA student OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: course_instructors; Type: TABLE; Schema: academics; Owner: postgres
--

CREATE TABLE academics.course_instructors (
    course_id character varying(20) NOT NULL,
    instructor_id character varying(20) NOT NULL
);


ALTER TABLE academics.course_instructors OWNER TO postgres;

--
-- Name: courses; Type: TABLE; Schema: academics; Owner: postgres
--

CREATE TABLE academics.courses (
    course_id character varying(20) NOT NULL,
    course_name character varying(100) NOT NULL,
    credits integer NOT NULL
);


ALTER TABLE academics.courses OWNER TO postgres;

--
-- Name: enrollments; Type: TABLE; Schema: academics; Owner: postgres
--

CREATE TABLE academics.enrollments (
    enrollment_id integer NOT NULL,
    student_id character varying(20) NOT NULL,
    course_id character varying(20) NOT NULL,
    enrollment_date date NOT NULL
);


ALTER TABLE academics.enrollments OWNER TO postgres;

--
-- Name: enrollments_enrollment_id_seq; Type: SEQUENCE; Schema: academics; Owner: postgres
--

CREATE SEQUENCE academics.enrollments_enrollment_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE academics.enrollments_enrollment_id_seq OWNER TO postgres;

--
-- Name: enrollments_enrollment_id_seq; Type: SEQUENCE OWNED BY; Schema: academics; Owner: postgres
--

ALTER SEQUENCE academics.enrollments_enrollment_id_seq OWNED BY academics.enrollments.enrollment_id;


--
-- Name: instructors; Type: TABLE; Schema: academics; Owner: postgres
--

CREATE TABLE academics.instructors (
    instructor_id character varying(20) NOT NULL,
    instructor_name character varying(100) NOT NULL,
    department character varying(100) NOT NULL
);


ALTER TABLE academics.instructors OWNER TO postgres;

--
-- Name: students_unt_student_id_seq; Type: SEQUENCE; Schema: student; Owner: postgres
--

CREATE SEQUENCE student.students_unt_student_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE student.students_unt_student_id_seq OWNER TO postgres;

--
-- Name: students_unt; Type: TABLE; Schema: student; Owner: postgres
--

CREATE TABLE student.students_unt (
    student_id character varying(30) DEFAULT ('UNT_2025_'::text || lpad((nextval('student.students_unt_student_id_seq'::regclass))::text, 4, '0'::text)) NOT NULL,
    full_name character varying(100) NOT NULL,
    email character varying(200),
    course character varying(100),
    age integer,
    student_join_year integer,
    is_active boolean DEFAULT true,
    address text,
    start_date date,
    end_date date
);


ALTER TABLE student.students_unt OWNER TO postgres;

--
-- Name: students_student_id_seq; Type: SEQUENCE; Schema: student; Owner: postgres
--

CREATE SEQUENCE student.students_student_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE student.students_student_id_seq OWNER TO postgres;

--
-- Name: students_student_id_seq; Type: SEQUENCE OWNED BY; Schema: student; Owner: postgres
--

ALTER SEQUENCE student.students_student_id_seq OWNED BY student.students_unt.student_id;


--
-- Name: enrollments enrollment_id; Type: DEFAULT; Schema: academics; Owner: postgres
--

ALTER TABLE ONLY academics.enrollments ALTER COLUMN enrollment_id SET DEFAULT nextval('academics.enrollments_enrollment_id_seq'::regclass);


--
-- Name: course_instructors course_instructors_pkey; Type: CONSTRAINT; Schema: academics; Owner: postgres
--

ALTER TABLE ONLY academics.course_instructors
    ADD CONSTRAINT course_instructors_pkey PRIMARY KEY (course_id, instructor_id);


--
-- Name: courses courses_pkey; Type: CONSTRAINT; Schema: academics; Owner: postgres
--

ALTER TABLE ONLY academics.courses
    ADD CONSTRAINT courses_pkey PRIMARY KEY (course_id);


--
-- Name: enrollments enrollments_pkey; Type: CONSTRAINT; Schema: academics; Owner: postgres
--

ALTER TABLE ONLY academics.enrollments
    ADD CONSTRAINT enrollments_pkey PRIMARY KEY (enrollment_id);


--
-- Name: instructors instructors_pkey; Type: CONSTRAINT; Schema: academics; Owner: postgres
--

ALTER TABLE ONLY academics.instructors
    ADD CONSTRAINT instructors_pkey PRIMARY KEY (instructor_id);


--
-- Name: students_unt students_pkey; Type: CONSTRAINT; Schema: student; Owner: postgres
--

ALTER TABLE ONLY student.students_unt
    ADD CONSTRAINT students_pkey PRIMARY KEY (student_id);


--
-- Name: course_instructors fk_course_instructor_course; Type: FK CONSTRAINT; Schema: academics; Owner: postgres
--

ALTER TABLE ONLY academics.course_instructors
    ADD CONSTRAINT fk_course_instructor_course FOREIGN KEY (course_id) REFERENCES academics.courses(course_id);


--
-- Name: course_instructors fk_course_instructor_instructor; Type: FK CONSTRAINT; Schema: academics; Owner: postgres
--

ALTER TABLE ONLY academics.course_instructors
    ADD CONSTRAINT fk_course_instructor_instructor FOREIGN KEY (instructor_id) REFERENCES academics.instructors(instructor_id);


--
-- Name: enrollments fk_enrollment_course; Type: FK CONSTRAINT; Schema: academics; Owner: postgres
--

ALTER TABLE ONLY academics.enrollments
    ADD CONSTRAINT fk_enrollment_course FOREIGN KEY (course_id) REFERENCES academics.courses(course_id);


--
-- Name: enrollments fk_enrollment_student; Type: FK CONSTRAINT; Schema: academics; Owner: postgres
--

ALTER TABLE ONLY academics.enrollments
    ADD CONSTRAINT fk_enrollment_student FOREIGN KEY (student_id) REFERENCES student.students_unt(student_id);


--
-- PostgreSQL database dump complete
--

\unrestrict OYLdlBj3GQk2ivxrqaBytnL96Qvq5rh7ROGLyMOsX37nyJUzDDxLhU6rpHqZV3R

