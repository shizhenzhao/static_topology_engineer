import sys
import numpy as np

def ReadOptimalKFilesIdx(file_dir, idx):
	fabrics_gap_optimalK = {}
	fabric_silhouette_optimalK = {}
	fabrics_order = []
	offset = 0
	filename = "optimalK_12fabs_idx_" + str(idx) + ".txt"
	with open(file_dir + filename, 'r') as f:
		for line in f:
			splitted_line = line.split()
			if offset == 0:
				for fab_name in splitted_line:
					fabrics_gap_optimalK[fab_name] = 0
					fabric_silhouette_optimalK[fab_name] = 0
					fabrics_order.append(fab_name)
				offset += 1
			elif offset == 1:
				fab_id = 0
				for optimalK in splitted_line:
					fabrics_gap_optimalK[fabrics_order[fab_id]] = int(optimalK)
					fab_id += 1
				offset += 1
			else:
				fab_id = 0
				for optimalK in splitted_line:
					fabric_silhouette_optimalK[fabrics_order[fab_id]] = int(optimalK)
					fab_id += 1
	return fabrics_gap_optimalK, fabric_silhouette_optimalK


def ReadOptimalKFiles(file_dir, indices):
	fabrics_gap_optimalK, fabric_silhouette_optimalK = ReadOptimalKFilesIdx(file_dir, indices[0])
	all_fabrics_optimalK_gap = {}
	all_fabrics_optimalK_silhouette = {}
	for fab_name in fabrics_gap_optimalK.keys():
		all_fabrics_optimalK_gap[fab_name] = [fabrics_gap_optimalK[fab_name]]
		all_fabrics_optimalK_silhouette[fab_name] = [fabric_silhouette_optimalK[fab_name]]
	for i in range(1, len(indices), 1):
		fabrics_gap_optimalK, fabric_silhouette_optimalK = ReadOptimalKFilesIdx(file_dir, indices[i])
		for fab_name in fabrics_gap_optimalK.keys():
			all_fabrics_optimalK_gap[fab_name].append(fabrics_gap_optimalK[fab_name])
			all_fabrics_optimalK_silhouette[fab_name].append(fabric_silhouette_optimalK[fab_name])
	return all_fabrics_optimalK_gap, all_fabrics_optimalK_silhouette

dirname = "/Users/minyee/static_topology_engineer/plot_data/"
indices = [1,2,3,4,5,6,7,8,9]

fabrics_optimalK_gap, fabrics_optimalK_silhouette = ReadOptimalKFiles(dirname, indices)
for fab in sorted(fabrics_optimalK_gap.keys()):
	std_dev_gap = np.std(fabrics_optimalK_gap[fab])
	std_dev_silhouette = np.std(fabrics_optimalK_silhouette[fab])
	mean_gap = np.mean(fabrics_optimalK_gap[fab])
	mean_silhouette = np.mean(fabrics_optimalK_silhouette[fab])
	median_gap = np.median(fabrics_optimalK_gap[fab])
	median_silhouette = np.median(fabrics_optimalK_silhouette[fab])
	max_gap = max(fabrics_optimalK_gap[fab])
	max_silhouette = max(fabrics_optimalK_silhouette[fab])
	min_gap = min(fabrics_optimalK_gap[fab])
	min_silhouette = min(fabrics_optimalK_silhouette[fab])
	str_builder = fab + "\ngap:\n"
	str_builder += ("mean: " + str(mean_gap) + " stddev: " + str(std_dev_gap) + " median: " + str(median_gap) + " max: " + str(max_gap) + " min: " + str(min_gap) + "\n")
	str_builder += "silhouette:\n"
	str_builder += ("mean: " + str(mean_silhouette) + " stddev: " + str(std_dev_silhouette) + " median: " + str(median_silhouette) + " max: " + str(max_silhouette) + " min: " + str(min_silhouette) + "\n\n\n")
	print str_builder
for fab in sorted(fabrics_optimalK_gap.keys()):
	print fabrics_optimalK_gap[fab]
	print fabrics_optimalK_silhouette[fab]