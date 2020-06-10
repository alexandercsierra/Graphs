import random

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)





class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()
    
    def get_friends(self, user_id):
        return self.friendships[user_id]

    def bft(self, user_id, head):
        #uses a queue
        start = user_id
        q = Queue()
        q.enqueue([user_id])

        visited = set()
        # visited.add(start)
        paths = []
        while q.size() > 0:
            #deq current
            current = q.dequeue()
            #add current vertex to visited if it isn't already there
            if current[-1] not in visited:
                # print('current friend', current[-1])
                # print('current', current)
                paths.append(current)
                visited.add(current[-1])

                #add all neighbors to q
                for vert in self.get_friends(current[-1]):
                    # print('vert', vert)
                    if vert != head:
                        new_path = [*current, vert]
                        q.enqueue(new_path)

        # print('returned path', paths)
        return paths



    def populate_graph(self, num_users, avg_friendships):
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # Add users
        for i in range(0, num_users):
            self.add_user(f"User {i}")
        # Create Frienships
        # Generate all possible friendship combinations
        possible_friendships = []

        # Avoid duplicates by ensuring the first number is smaller than the second
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))
                
            # Shuffle the possible friendships
            random.shuffle(possible_friendships)
        # Create friendships for the first X pairs of the list
        # X is determined by the formula: num_users * avg_friendships // 2
        # Need to divide by 2 since each add_friendship() creates 2 friendships


        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])
        
            


    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {user_id: [user_id]}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME

        #each key is a friend and each value is the path to that friend

        friendships = self.friendships[user_id]
        paths_list = []

        if len(friendships) > 0:
            for friend in friendships:
                # print('friend', friend)
                # print(self.bft(friend))
                # paths[friend] = self.bft(friend, user_id)

                path = self.bft(friend, user_id)
                paths_list += path

            for path in paths_list:
                last_num = path[-1]

                if last_num not in visited:
                    visited[last_num] = [user_id, *path]
                else:
                    if len(path) < len(visited[last_num])-1:
                        visited[last_num] = [user_id, *path]
            
        



        return visited


'''

{1: {8, 10, 5}, 2: {10, 5, 7}, 3: {4}, 4: {9, 3}, 5: {8, 1, 2}, 6: {10}, 7: {2}, 8: {1, 5}, 9: {4}, 10: {1, 2, 6}}



{1: [1], 8: [1, 8], 10: [1, 10], 5: [1, 5], 2: [1, 10, 2], 6: [1, 10, 6], 7: [1, 10, 2, 7]}
'''

if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print('friendships', sg.friendships)
    connections = sg.get_all_social_paths(1)
    print('connections', connections)
    print("\n")

    g = SocialGraph()
    g.add_user(1)
    g.add_user(2)
    g.add_user(3)
    g.add_user(4)
    g.add_user(5)
    g.add_user(6)
    g.add_user(7)
    g.add_user(8)
    g.add_user(9)
    g.add_user(10)

    g.add_friendship(1,8)
    g.add_friendship(1,10)
    g.add_friendship(1,5)
    g.add_friendship(2,10)
    g.add_friendship(2,5)
    g.add_friendship(2,7)
    g.add_friendship(3,4)
    g.add_friendship(4,9)
    g.add_friendship(5,8)
    g.add_friendship(6,10)

    print('friendships', g.friendships)
    print('connections', g.get_all_social_paths(1))



'''

{1: {8, 10, 5}, 2: {10, 5, 7}, 3: {4}, 4: {9, 3}, 5: {8, 1, 2}, 6: {10}, 7: {2}, 8: {1, 5}, 9: {4}, 10: {1, 2, 6}}



{1: [1], 8: [1, 8], 10: [1, 10], 5: [1, 5], 2: [1, 10, 2], 6: [1, 10, 6], 7: [1, 10, 2, 7]}
'''

    
