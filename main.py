if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))

    def runner_up(item):
        unique_arr = list(set(sorted((item), reverse=True)))

        if len(unique_arr) < 2:
            return None

        unique_arr.sort(reverse=True)

        return unique_arr[1]

    print(runner_up(arr))
