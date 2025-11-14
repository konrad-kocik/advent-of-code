from password_manager import change_password

print('Solving first part of puzzle')
new_password = change_password(old_password='hepxcrrq')
print(f'Answer to first part of puzzle is: {new_password}')

print('Solving second part of puzzle')
new_password = change_password(old_password=new_password)
print(f'Answer to second part of puzzle is: {new_password}')
