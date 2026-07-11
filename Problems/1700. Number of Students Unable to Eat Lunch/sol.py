class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        refusals = 0
        while students:
            if sandwiches[0] == students[0]:
                sandwiches.pop(0)
                students.pop(0)
                refusals = 0
            else:
                val = students.pop(0)
                students.append(val)
                refusals += 1
            
            if refusals == len(students):
                break

        return len(students)