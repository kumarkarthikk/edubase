"""
models.py
----------
This file defines all the tables in our database.
Each class here = one table. Each variable inside = one column.

We have one User table for login (shared by all 4 roles), and
separate tables for school data: students, teachers, attendance,
marks, fees, leave requests, and announcements.
"""

from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, DateTime, Text, Date
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime


class User(Base):
    """
    Login table — used by ALL 4 portals.
    The 'role' column decides what kind of user this is:
    'principal', 'staff', 'admin', or 'parent_student'
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String, default="")
    role = Column(String, nullable=False)   # principal / staff / admin / parent_student
    created_at = Column(DateTime, default=datetime.utcnow)
    is_active = Column(Boolean, default=True)


class Teacher(Base):
    """Teacher records — managed by Principal"""
    __tablename__ = "teachers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    subject = Column(String, default="")
    phone = Column(String, default="")
    email = Column(String, default="")
    assigned_class = Column(String, default="")   # e.g. "10th A"
    created_at = Column(DateTime, default=datetime.utcnow)


class SchoolClass(Base):
    """Classes/sections — e.g. 10th A, 9th B"""
    __tablename__ = "classes"

    id = Column(Integer, primary_key=True, index=True)
    class_name = Column(String, nullable=False)     # e.g. "10th"
    section = Column(String, default="A")            # e.g. "A"
    class_teacher_id = Column(Integer, ForeignKey("teachers.id"), nullable=True)

    students = relationship("Student", back_populates="school_class")


class Student(Base):
    """Student records — managed by Admin, viewed by Parent/Student"""
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    father_name = Column(String, default="")
    phone = Column(String, default="")
    class_id = Column(Integer, ForeignKey("classes.id"), nullable=True)
    admission_date = Column(DateTime, default=datetime.utcnow)
    is_active = Column(Boolean, default=True)   # False = left the school

    school_class = relationship("SchoolClass", back_populates="students")
    attendance_records = relationship("Attendance", back_populates="student")
    marks_records = relationship("Marks", back_populates="student")
    fee_records = relationship("Fee", back_populates="student")
    leave_requests = relationship("LeaveRequest", back_populates="student")


class Attendance(Base):
    """Daily attendance — marked by Staff, viewed by Parent/Student"""
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    date = Column(Date, default=datetime.utcnow().date)
    status = Column(String, default="present")   # present / absent

    student = relationship("Student", back_populates="attendance_records")


class Marks(Base):
    """Exam marks — entered by Staff, viewed by Parent/Student"""
    __tablename__ = "marks"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    subject = Column(String, nullable=False)
    exam_name = Column(String, default="")   # e.g. "Midterm"
    marks_obtained = Column(Float, nullable=False)
    max_marks = Column(Float, default=100)

    student = relationship("Student", back_populates="marks_records")


class Fee(Base):
    """Fee records — managed by Admin, viewed by Parent/Student"""
    __tablename__ = "fees"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    total_amount = Column(Float, nullable=False)
    paid_amount = Column(Float, default=0)
    due_date = Column(Date, nullable=True)
    is_paid = Column(Boolean, default=False)

    student = relationship("Student", back_populates="fee_records")


class LeaveRequest(Base):
    """
    Leave requests — can be submitted by a Student (via parent portal)
    or a Staff member. Approved/rejected by Principal.
    """
    __tablename__ = "leave_requests"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=True)
    teacher_id = Column(Integer, ForeignKey("teachers.id"), nullable=True)
    reason = Column(Text, nullable=False)
    from_date = Column(Date, nullable=False)
    to_date = Column(Date, nullable=False)
    status = Column(String, default="pending")   # pending / approved / rejected
    created_at = Column(DateTime, default=datetime.utcnow)

    student = relationship("Student", back_populates="leave_requests")


class Announcement(Base):
    """Notices posted by Principal, visible to everyone"""
    __tablename__ = "announcements"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    message = Column(Text, nullable=False)
    posted_by = Column(String, default="Principal")
    created_at = Column(DateTime, default=datetime.utcnow)