from fastapi import FastAPI
from routes.users_routes import router as users_router
from routes.parameters_values_routes import router as parameters_values_router
from routes.parameters_routes import router as parameters_router
from routes.schools_users_routes import router as schools_users_router
from routes.participants_activities_routes import router as participants_activities_router
from routes.participants_meetings_routes import router as participants_meetings_router
from routes.schools_routes import router as schools_router
from routes.roles_routes import router as roles_router
from routes.activities_routes import router as activities_router
from routes.comments_activities_routers import router as comments_activities_router
from routes.evidence_activities_routers import router as evidence_activities_router
from routes.meetings_routers import router as meetings_router
from routes.reports_routes import router as reports_router
from routes.reports_evidencies_routes import router as reports_evidencies_router
from routes.auth_routes import router as auth_router
from routes.modules_routes import router as modules_router
from routes.permissions_routes import router as permissions_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    #"http://localhost.tiangolo.com",
    #"https://localhost.tiangolo.com",
    "http://localhost"
    #"http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users_router)
app.include_router(parameters_values_router)
app.include_router(parameters_router)
app.include_router(schools_users_router)
app.include_router(participants_activities_router)
app.include_router(participants_meetings_router)
app.include_router(schools_router)
app.include_router(roles_router)
app.include_router(activities_router)
app.include_router(comments_activities_router)
app.include_router(evidence_activities_router)
app.include_router(meetings_router)
app.include_router(reports_router)
app.include_router(reports_evidencies_router)
app.include_router(auth_router)
app.include_router(modules_router)
app.include_router(permissions_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)