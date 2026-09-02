from sqlalchemy import (
    create_engine,
    String,
    ForeignKey,
    Table,
    Column,
    select,
)

from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship,
    Session,
    selectinload,
)


# ============================================================
# DATABASE
# ============================================================

engine = create_engine("sqlite:///test.db")


# ============================================================
# BASE
# ============================================================

class Base(DeclarativeBase):
    pass


# ============================================================
# ONE-TO-MANY RELATIONSHIP
# User -> Posts
#
# One User can have many Posts.
# ============================================================

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    age: Mapped[int]

    # One User -> Many Posts
    posts: Mapped[list["Post"]] = relationship(
        back_populates="user"
    )


class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200))

    # Foreign Key connects posts.user_id to users.id
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )

    # Many Posts -> One User
    user: Mapped["User"] = relationship(
        back_populates="posts"
    )


# ============================================================
# MANY-TO-MANY RELATIONSHIP
# Student <-> Course
# ============================================================

# Association table
student_courses = Table(
    "student_courses",
    Base.metadata,

    Column(
        "student_id",
        ForeignKey("students.id"),
        primary_key=True
    ),

    Column(
        "course_id",
        ForeignKey("courses.id"),
        primary_key=True
    )
)


class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))

    # Many Students <-> Many Courses
    courses: Mapped[list["Course"]] = relationship(
        secondary=student_courses,
        back_populates="students"
    )


class Course(Base):
    __tablename__ = "courses"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))

    # Many Courses <-> Many Students
    students: Mapped[list["Student"]] = relationship(
        secondary=student_courses,
        back_populates="courses"
    )


# ============================================================
# CREATE TABLES
# ============================================================

Base.metadata.create_all(engine)


# ============================================================
# CREATE USERS
# ============================================================

with Session(engine) as session:

    user1 = User(name="Ali", age=20)
    user2 = User(name="Sara", age=25)

    session.add_all([user1, user2])
    session.commit()


# ============================================================
# READ USERS
# ============================================================

with Session(engine) as session:

    users = session.execute(
        select(User)
    ).scalars().all()

    for user in users:
        print(user.id, user.name, user.age)


# ============================================================
# FIND USER
# ============================================================

with Session(engine) as session:

    user = session.get(User, 1)

    if user:
        print(user.name, user.age)


# ============================================================
# UPDATE USER
# ============================================================

with Session(engine) as session:

    user = session.get(User, 1)

    if user:
        user.age = 21
        session.commit()


# ============================================================
# DELETE USER
# ============================================================

with Session(engine) as session:

    user = session.get(User, 2)

    if user:
        session.delete(user)
        session.commit()


# ============================================================
# ADD RELATIONSHIP SAMPLE DATA
# ============================================================

with Session(engine) as session:

    # Check whether User 1 exists
    user = session.get(User, 1)

    if user:

        # Check if the user already has posts
        if not user.posts:

            post1 = Post(
                title="My first post",
                user=user
            )

            post2 = Post(
                title="Learning SQLAlchemy",
                user=user
            )

            session.add_all([post1, post2])


    # Students
    student1 = Student(name="John")
    student2 = Student(name="Mike")

    # Courses
    python_course = Course(name="Python")
    sql_course = Course(name="SQL")

    # Many-to-many relationships
    student1.courses.append(python_course)
    student1.courses.append(sql_course)

    student2.courses.append(sql_course)

    session.add_all([
        student1,
        student2,
        python_course,
        sql_course,
    ])

    session.commit()


# ============================================================
# WHERE
# ============================================================

with Session(engine) as session:

    statement = select(User).where(
        User.age >= 21
    )

    users = session.execute(
        statement
    ).scalars().all()

    for user in users:
        print(user.name)


# ============================================================
# USER -> POSTS
# ONE-TO-MANY
# ============================================================

with Session(engine) as session:

    user = session.get(User, 1)

    if user:

        print(user.name)

        for post in user.posts:
            print(post.title)


# ============================================================
# POST -> USER
# MANY-TO-ONE
# ============================================================

with Session(engine) as session:

    post = session.get(Post, 1)

    if post:

        print(post.title)
        print(post.user.name)


# ============================================================
# STUDENT -> COURSES
# MANY-TO-MANY
# ============================================================

with Session(engine) as session:

    student = session.get(Student, 1)

    if student:

        print(student.name)

        for course in student.courses:
            print(course.name)


# ============================================================
# COURSE -> STUDENTS
# MANY-TO-MANY
# ============================================================

with Session(engine) as session:

    course = session.get(Course, 1)

    if course:

        print(course.name)

        for student in course.students:
            print(student.name)


# ============================================================
# JOIN
# ============================================================

with Session(engine) as session:

    statement = (
        select(User, Post)
        .join(
            Post,
            User.id == Post.user_id
        )
    )

    results = session.execute(
        statement
    ).all()

    for user, post in results:

        print(
            user.name,
            "->",
            post.title
        )


# ============================================================
# SELECTINLOAD
#
# Load Users and their Posts efficiently.
# Helps avoid the N+1 query problem.
# ============================================================

with Session(engine) as session:

    statement = (
        select(User)
        .options(
            selectinload(User.posts)
        )
    )

    users = session.execute(
        statement
    ).scalars().all()

    for user in users:

        print(user.name)

        for post in user.posts:
            print(post.title)