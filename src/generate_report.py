from ydata_profiling.profile_report import ProfileReport

def generate_report(df):
    report = ProfileReport(df, explorative=True)
    report.to_file("titanic_data.html")