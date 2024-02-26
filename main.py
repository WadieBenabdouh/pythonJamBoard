ff = "Firefox Developer Edition "
brave = "Brave Browser "
benchmarkTest = ["SpotifyTab", "YouTubeTab", "ChatGPTTab"]

memoryUsage = "RAM"

resutlFF = ff + str(benchmarkTest) + " = " + str(83) + "%"
resultBB = brave + str(benchmarkTest) + " = " + str(70) + "%"

finalVerdict = [resutlFF] + [resultBB]
print(finalVerdict)