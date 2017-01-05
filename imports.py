from flask import Flask, render_template, flash, request, url_for, redirect
# from flask import abort
# from flask import make_response
from flask_httpauth import HTTPBasicAuth
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask.ext.security import Security, SQLAlchemyUserDatastore, \
    UserMixin, RoleMixin, login_required
import psycopg2  
 