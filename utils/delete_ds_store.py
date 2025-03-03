import os

def delete_ds_store(directory):

    deleted_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file == ".DS_Store":
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    deleted_files.append(file_path)
                except Exception as e:
                    print(f"刪除失敗: {file_path}，錯誤: {e}")
    
    return deleted_files

if __name__ == "__main__":
    base_directory = os.path.dirname(os.path.abspath(__file__))  
    print(f"掃描目錄: {base_directory}\n")

    projects = [d for d in os.listdir(base_directory) if os.path.isdir(os.path.join(base_directory, d)) and not d.startswith(".")]

    if not projects:
        print("沒有發現任何專案資料夾，請確認專案是否放在此腳本的同一層！")
    else:
        for project in projects:
            project_path = os.path.join(base_directory, project)
            print(f"正在掃描專案: {project_path}")

            deleted_files = delete_ds_store(project_path)

            if deleted_files:
                print("已刪除的 .DS_Store 檔案:")
                for file in deleted_files:
                    print(f"   - {file}")
            else:
                print("沒有發現 .DS_Store 檔案")

    print("\n所有專案掃描完成！")


# 刪除該目錄下的所有資料夾內的 .DS_Store 檔