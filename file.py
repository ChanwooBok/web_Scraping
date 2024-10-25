import csv



def save_to_file(file_name,jobs_list):

    with open(f"{file_name}.csv", "w", newline="", encoding="utf-8") as file:  # Use 'with' for better file handling
        writer = csv.writer(file)
        writer.writerow(["Title", "Company"])  # Header

        for job in jobs_list:
            writer.writerow(job.values())