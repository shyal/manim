
type = 'dev'
sync = true
open = false

ifeq ($(type),prod)
	RES = 1440p60
	FLAGS = ''
else
	RES = 480p15
	FLAGS = '-pl'
endif

ENV = INPUT_PATH=`pwd` OUTPUT_PATH=`pwd` 

all: 	linked_list_cycle \
		sublist \
		merge \
		add_two_numbers \
		buildings \
		merge_accounts \
		drone \
		longest_arith \
		stock \
		dfs \
		validate_sudoku \
		solve_sudoku \
		subarray_sum \
		primes \
		array_index_element \
		lev \
		islands \
		celebrity \
		rabin_karp \
		bitcoin \
		assetview


%.gif: %.mp4
	echo $^
# 	ffmpeg -y -i $^ -r 15 -vf scale=1024:-1 media/$@
# 	if ${sync}; then aws s3 cp media/$@ s3://manim; fi

entries:
	python3 entries.py `ls videos/*/1440p60/*.mp4`
	rsync -azv manifest.json entries.json root@ioloop.io:/home/static/pythonical_videos/

gifs:
	for f in videos/*/1440p60/*.mp4; do make "$${f%%.*}.gif"; done

list_gifs:
	for f in videos/*/1440p60/*.mp4; do ls "$${f%%.*}.gif"; done

bitcoin: videos/bitcoin_relative_volatility/${RES}/BitcoinRelativeVolatility.mp4

assetview: videos/assetview_logo/${RES}/AssetViewLogo.mp4

.PHONY: btc.json

btc.json:
	python3 get_btc_prices.py

videos/bitcoin_relative_volatility/${RES}/BitcoinRelativeVolatility.mp4: bitcoin_relative_volatility.py btc.json
	${ENV} ./manim.py bitcoin_relative_volatility.py BitcoinRelativeVolatility ${FLAGS}
	if ${sync}; then aws s3 cp media/$@ s3://manim; fi
	if ${open}; then open $@; fi

videos/assetview_logo/${RES}/AssetViewLogo.mp4: assetview_logo.py btc.json
	${ENV} ./manim.py assetview_logo.py AssetViewLogo ${FLAGS}
	if ${sync}; then aws s3 cp media/$@ s3://manim; fi
	if ${open}; then open $@; fi

videos/bitcoin/${RES}/BitcoinHalvingDefault.mp4: bitcoin.py btc.json
	${ENV} ./manim.py bitcoin.py BitcoinHalvingDefault ${FLAGS}
	if ${sync}; then aws s3 cp media/$@ s3://manim; fi
	if ${open}; then open $@; fi

videos/bitcoin/${RES}/BitcoinHalvingsGMI.mp4: bitcoin.py btc.json
	${ENV} ./manim.py bitcoin.py BitcoinHalvingsGMI ${FLAGS}
	if ${sync}; then aws s3 cp media/$@ s3://manim; fi
	if ${open}; then open $@; fi

videos/bitcoin/${RES}/BitcoinHalvingsASK.mp4: bitcoin.py btc.json
	${ENV} ./manim.py bitcoin.py BitcoinHalvingsASK ${FLAGS}
	if ${sync}; then aws s3 cp media/$@ s3://manim; fi
	if ${open}; then open $@; fi

videos/bitcoin/${RES}/BitcoinHalvingsMoneyPuzzle.mp4: bitcoin.py btc.json
	${ENV} ./manim.py bitcoin.py BitcoinHalvingsMoneyPuzzle ${FLAGS}
	if ${sync}; then aws s3 cp media/$@ s3://manim; fi
	if ${open}; then open $@; fi

rabin_karp: \
			videos/rabin_karp/${RES}/RabinRollingHash.mp4 \
			videos/rabin_karp/${RES}/RabinHashReorgEquation.mp4 \
			videos/rabin_karp/${RES}/RabinHashBasicEquation.mp4 \
			videos/rabin_karp/${RES}/RabinSlidingSimple.mp4 \
			videos/rabin_karp/${RES}/StringHash.mp4 \
			videos/rabin_karp/${RES}/SentenceHash.mp4

videos/rabin_karp/${RES}/RabinRollingHash.mp4: rabin_karp.py logo.py
	${ENV} ./manim.py rabin_karp.py RabinRollingHash ${FLAGS}
	if ${sync}; then aws s3 cp media/$@ s3://manim; fi
	if ${open}; then open $@; fi

videos/rabin_karp/${RES}/RabinHashReorgEquation.mp4: rabin_karp.py logo.py
	${ENV} ./manim.py rabin_karp.py RabinHashReorgEquation ${FLAGS}
	if ${sync}; then aws s3 cp media/$@ s3://manim; fi
	if ${open}; then open $@; fi

videos/rabin_karp/${RES}/RabinHashBasicEquation.mp4: rabin_karp.py logo.py
	${ENV} ./manim.py rabin_karp.py RabinHashBasicEquation ${FLAGS}
	if ${sync}; then aws s3 cp media/$@ s3://manim; fi
	if ${open}; then open $@; fi

videos/rabin_karp/${RES}/RabinSlidingSimple.mp4: rabin_karp.py logo.py
	${ENV} ./manim.py rabin_karp.py RabinSlidingSimple ${FLAGS}
	if ${sync}; then aws s3 cp media/$@ s3://manim; fi
	if ${open}; then open $@; fi

videos/rabin_karp/${RES}/StringHash.mp4: rabin_karp.py logo.py
	${ENV} ./manim.py rabin_karp.py StringHash ${FLAGS}
	if ${sync}; then aws s3 cp media/$@ s3://manim; fi
	if ${open}; then open $@; fi

videos/rabin_karp/${RES}/SentenceHash.mp4: rabin_karp.py logo.py
	${ENV} ./manim.py rabin_karp.py SentenceHash ${FLAGS}
	if ${sync}; then aws s3 cp media/$@ s3://manim; fi
	if ${open}; then open $@; fi


linked_list_cycle:  \
					videos/linked_list_cycle/${RES}/LinkedListCycleStartNode.mp4 \
					videos/linked_list_cycle/${RES}/LinkedListCycleStartNode.gif \
					videos/linked_list_cycle/${RES}/LinkedListCycleFastSlow.mp4 \
					videos/linked_list_cycle/${RES}/LinkedListCycleFastSlow.gif \
					videos/linked_list_cycle/${RES}/LinkedListCyclePlain.mp4 \
					videos/linked_list_cycle/${RES}/LinkedListCyclePlain.gif \

videos/linked_list_cycle/${RES}/LinkedListCycleStartNode.mp4: linked_list_cycle.py logo.py linked_list.py
	${ENV} ./manim.py linked_list_cycle.py LinkedListCycleStartNode ${FLAGS}
	if ${sync}; then aws s3 cp media/$@ s3://manim; fi
	if ${open}; then open $@; fi

videos/linked_list_cycle/${RES}/LinkedListCyclePlain.mp4: linked_list_cycle.py logo.py linked_list.py
	${ENV} ./manim.py linked_list_cycle.py LinkedListCyclePlain ${FLAGS}
	if ${sync}; then aws s3 cp media/$@ s3://manim; fi
	if ${open}; then open $@; fi

videos/linked_list_cycle/${RES}/LinkedListCycleFastSlow.mp4: linked_list_cycle.py logo.py linked_list.py
	${ENV} ./manim.py linked_list_cycle.py LinkedListCycleFastSlow ${FLAGS}
	if ${sync}; then aws s3 cp media/$@ s3://manim; fi
	if ${open}; then open $@; fi

sublist: 	videos/reverse_sublist/${RES}/ReverseSublist1.mp4 \
			videos/reverse_sublist/${RES}/ReverseSublistCreation.mp4 \
			videos/reverse_sublist/${RES}/ReverseSublistTail.mp4 \
			videos/reverse_sublist/${RES}/ReverseSublistTailStaticTmpMoving.mp4 \
			videos/reverse_sublist/${RES}/ReverseSublistTailStatic.mp4

videos/reverse_sublist/${RES}/ReverseSublistTailStaticTmpMoving.mp4: reverse_sublist.py logo.py linked_list.py
	${ENV} ./manim.py reverse_sublist.py ReverseSublistTailStaticTmpMoving ${FLAGS}
	if ${sync}; then aws s3 cp media/$@ s3://manim; fi
	if ${open}; then open $@; fi

videos/reverse_sublist/${RES}/ReverseSublistTailStatic.mp4: reverse_sublist.py logo.py linked_list.py
	${ENV} ./manim.py reverse_sublist.py ReverseSublistTailStatic ${FLAGS}
	if ${sync}; then aws s3 cp media/$@ s3://manim; fi
	if ${open}; then open $@; fi

videos/reverse_sublist/${RES}/ReverseSublistCreation.mp4: reverse_sublist.py logo.py linked_list.py
	${ENV} ./manim.py reverse_sublist.py ReverseSublistCreation ${FLAGS}
	if ${sync}; then aws s3 cp media/$@ s3://manim; fi
	if ${open}; then open $@; fi

videos/reverse_sublist/${RES}/ReverseSublistTail.mp4: reverse_sublist.py logo.py linked_list.py
	${ENV} ./manim.py reverse_sublist.py ReverseSublistTail ${FLAGS}
	if ${sync}; then aws s3 cp media/$@ s3://manim; fi
	if ${open}; then open $@; fi

videos/reverse_sublist/${RES}/ReverseSublist1.mp4: reverse_sublist.py logo.py linked_list.py
	${ENV} ./manim.py reverse_sublist.py ReverseSublist1 ${FLAGS}
	if ${sync}; then aws s3 cp media/$@ s3://manim; fi
	if ${open}; then open $@; fi


merge: 				videos/merge_k_sorted_lists/${RES}/MergeKSortedLists1.mp4

videos/merge_k_sorted_lists/${RES}/MergeKSortedLists1.mp4: merge_k_sorted_lists.py logo.py linked_list.py
	${ENV} ./manim.py merge_k_sorted_lists.py MergeKSortedLists1 ${FLAGS}
	if ${sync}; then aws s3 cp media/$@ s3://manim; fi
	if ${open}; then open $@; fi

add_two_numbers: 	videos/add_two_numbers/${RES}/AddTwoNumbers1.mp4 \
					videos/add_two_numbers/${RES}/AddTwoNumbers2.mp4 \
					videos/add_two_numbers/${RES}/AddTwoNumbers3.mp4 

videos/add_two_numbers/${RES}/AddTwoNumbers1.mp4: add_two_numbers.py logo.py linked_list.py
	${ENV} ./manim.py add_two_numbers.py AddTwoNumbers1 ${FLAGS}
	if ${sync}; then aws s3 cp media/$@ s3://manim; fi
	if ${open}; then open $@; fi

videos/add_two_numbers/${RES}/AddTwoNumbers2.mp4: add_two_numbers.py logo.py linked_list.py
	${ENV} ./manim.py add_two_numbers.py AddTwoNumbers2 ${FLAGS}
	if ${sync}; then aws s3 cp media/$@ s3://manim; fi
	if ${open}; then open $@; fi

videos/add_two_numbers/${RES}/AddTwoNumbers3.mp4: add_two_numbers.py logo.py linked_list.py
	${ENV} ./manim.py add_two_numbers.py AddTwoNumbers3 ${FLAGS}
	if ${sync}; then aws s3 cp media/$@ s3://manim; fi
	if ${open}; then open $@; fi

# videos/shortest_distance_from_all_buildings/${RES}/ShortestDistanceFromAllBuildings.gif: videos/shortest_distance_from_all_buildings/${RES}/ShortestDistanceFromAllBuildings.mp4
# 	ffmpeg \
# 	  -i videos/shortest_distance_from_all_buildings/${RES}/ShortestDistanceFromAllBuildings.mp4 \
# 	  -r 15 \
# 	  -y \
# 	  -vf scale=1024:-1 \
# 	  videos/shortest_distance_from_all_buildings/${RES}/ShortestDistanceFromAllBuildings.gif


buildings: 			videos/shortest_distance_from_all_buildings/${RES}/ShortestDistanceFromAllBuildings.mp4 \
					videos/shortest_distance_from_all_buildings/${RES}/ShortestDistanceFromAllBuildingsTotal.mp4 \
					videos/shortest_distance_from_all_buildings/${RES}/ShortestDistanceFromAllBuildingsFinal.mp4

videos/shortest_distance_from_all_buildings/${RES}/ShortestDistanceFromAllBuildingsFinal.mp4: shortest_distance_from_all_buildings.py logo.py
	${ENV} ./manim.py shortest_distance_from_all_buildings.py ShortestDistanceFromAllBuildingsFinal ${FLAGS}
	if ${sync}; then aws s3 cp media/$@ s3://manim; fi
	if ${open}; then open $@; fi

videos/shortest_distance_from_all_buildings/${RES}/ShortestDistanceFromAllBuildings.mp4: shortest_distance_from_all_buildings.py logo.py
	${ENV} ./manim.py shortest_distance_from_all_buildings.py ShortestDistanceFromAllBuildings ${FLAGS}
	if ${sync}; then aws s3 cp media/$@ s3://manim; fi
	if ${open}; then open $@; fi

videos/shortest_distance_from_all_buildings/${RES}/ShortestDistanceFromAllBuildingsTotal.mp4: shortest_distance_from_all_buildings.py logo.py
	${ENV} ./manim.py shortest_distance_from_all_buildings.py ShortestDistanceFromAllBuildingsTotal ${FLAGS}
	if ${sync}; then aws s3 cp media/$@ s3://manim; fi
	if ${open}; then open $@; fi

videos/binary_tree_right_side_view/${RES}/BinaryTreeRightSideView.mp4: binary_tree_right_side_view.py logo.py tree.py
	${ENV} ./manim.py binary_tree_right_side_view.py BinaryTreeRightSideView ${FLAGS}
	if ${sync}; then aws s3 cp media/$@ s3://manim; fi
	if ${open}; then open $@; fi

merge_accounts: videos/merge_accounts/${RES}/MergeAccounts.mp4

videos/merge_accounts/${RES}/MergeAccounts.mp4: merge_accounts.py logo.py my_manim_lib.py
	${ENV} ./manim.py merge_accounts.py MergeAccounts ${FLAGS}
	if ${sync}; then aws s3 cp media/$@ s3://manim; fi
	if ${open}; then open $@; fi

drone: 		videos/drone_flight_planner/${RES}/Drone3D.mp4 \
			videos/drone_flight_planner/${RES}/Drone2D.mp4 \
			videos/drone_flight_planner/${RES}/Drone2DSuccess.mp4 \
			videos/drone_flight_planner/${RES}/Drone2DHomeostasis.mp4 \

videos/drone_flight_planner/${RES}/Drone2DSuccess.mp4: drone_flight_planner.py logo.py my_manim_lib.py
	${ENV} ./manim.py drone_flight_planner.py Drone2DSuccess ${FLAGS}
	if ${sync}; then aws s3 cp media/$@ s3://manim; fi
	if ${open}; then open $@; fi

videos/drone_flight_planner/${RES}/Drone2D.mp4: drone_flight_planner.py logo.py my_manim_lib.py
	${ENV} ./manim.py drone_flight_planner.py Drone2D ${FLAGS}
	if ${sync}; then aws s3 cp media/$@ s3://manim; fi
	if ${open}; then open $@; fi

videos/drone_flight_planner/${RES}/Drone2DHomeostasis.mp4: drone_flight_planner.py logo.py my_manim_lib.py
	${ENV} ./manim.py drone_flight_planner.py Drone2DHomeostasis ${FLAGS}
	if ${sync}; then aws s3 cp media/$@ s3://manim; fi
	if ${open}; then open $@; fi

videos/drone_flight_planner/${RES}/Drone3D.mp4: drone_flight_planner.py logo.py my_manim_lib.py
	${ENV} ./manim.py drone_flight_planner.py Drone3D ${FLAGS}
	if ${sync}; then aws s3 cp media/$@ s3://manim; fi
	if ${open}; then open $@; fi

longest_arith: 	videos/longest_arithmetic_sequence/${RES}/LongestArithmeticSequenceFirst.mp4 \
				videos/longest_arithmetic_sequence/${RES}/LongestArithmeticSequenceIteration.mp4 \
				videos/longest_arithmetic_sequence/${RES}/LongestArithmeticSequenceProblemStatement.mp4 \

videos/longest_arithmetic_sequence/${RES}/LongestArithmeticSequenceProblemStatement.mp4: longest_arithmetic_sequence.py logo.py my_manim_lib.py
	${ENV} ./manim.py longest_arithmetic_sequence.py LongestArithmeticSequenceProblemStatement ${FLAGS}
	if ${sync}; then aws s3 cp media/$@ s3://manim; fi
	if ${open}; then open $@; fi

videos/longest_arithmetic_sequence/${RES}/LongestArithmeticSequenceFirst.mp4: longest_arithmetic_sequence.py logo.py
	${ENV} ./manim.py longest_arithmetic_sequence.py LongestArithmeticSequenceFirst ${FLAGS}
	if ${sync}; then aws s3 cp media/$@ s3://manim; fi
	if ${open}; then open $@; fi

videos/longest_arithmetic_sequence/${RES}/LongestArithmeticSequenceIteration.mp4: longest_arithmetic_sequence.py logo.py
	${ENV} ./manim.py longest_arithmetic_sequence.py LongestArithmeticSequenceIteration ${FLAGS}
	if ${sync}; then aws s3 cp media/$@ s3://manim; fi
	if ${open}; then open $@; fi

stock: videos/buy_and_sell_stock/${RES}/BestTimeToBuyAndSellStockMinPriceMarkers.mp4 videos/buy_and_sell_stock/${RES}/BestTimeToBuyAndSellStockSimplePrice.mp4 videos/buy_and_sell_stock/${RES}/BestTimeToBuyAndSellStockMinPrice.mp4 videos/buy_and_sell_stock/${RES}/BestTimeToBuyAndSellStockMinPriceMarkersTrade.mp4
	echo 'done'

videos/buy_and_sell_stock/${RES}/BestTimeToBuyAndSellStockMinPriceMarkers.mp4: buy_and_sell_stock.py logo.py
	${ENV} ./manim.py buy_and_sell_stock.py BestTimeToBuyAndSellStockMinPriceMarkers ${FLAGS}
	if ${sync}; then aws s3 cp media/$@ s3://manim; fi
	if ${open}; then open $@; fi

videos/buy_and_sell_stock/${RES}/BestTimeToBuyAndSellStockSimplePrice.mp4: buy_and_sell_stock.py logo.py
	${ENV} ./manim.py buy_and_sell_stock.py BestTimeToBuyAndSellStockSimplePrice ${FLAGS}
	if ${sync}; then aws s3 cp media/$@ s3://manim; fi
	if ${open}; then open $@; fi

videos/buy_and_sell_stock/${RES}/BestTimeToBuyAndSellStockMinPrice.mp4: buy_and_sell_stock.py logo.py
	${ENV} ./manim.py buy_and_sell_stock.py BestTimeToBuyAndSellStockMinPrice ${FLAGS}
	if ${sync}; then aws s3 cp media/$@ s3://manim; fi
	if ${open}; then open $@; fi

videos/buy_and_sell_stock/${RES}/BestTimeToBuyAndSellStockMinPriceMarkersTrade.mp4: buy_and_sell_stock.py logo.py
	${ENV} ./manim.py buy_and_sell_stock.py BestTimeToBuyAndSellStockMinPriceMarkersTrade ${FLAGS}
	if ${sync}; then aws s3 cp media/$@ s3://manim; fi
	if ${open}; then open $@; fi

videos/bfs/${RES}/BinaryTreeBFS.mp4: bfs.py logo.py
	${ENV} ./manim.py bfs.py BinaryTreeBFS ${FLAGS}
	if ${sync}; then aws s3 cp media/$@ s3://manim; fi
	if ${open}; then open $@; fi

dfs: videos/dfs/${RES}/PreOrder.mp4 videos/dfs/${RES}/InOrder.mp4 videos/dfs/${RES}/PostOrder.mp4 videos/bfs/${RES}/BinaryTreeBFS.mp4 \

videos/dfs/${RES}/PreOrder.mp4: dfs.py logo.py
	${ENV} ./manim.py dfs.py PreOrder ${FLAGS}
	if ${sync}; then aws s3 cp media/$@ s3://manim; fi
	if ${open}; then open $@; fi

videos/dfs/${RES}/InOrder.mp4: dfs.py logo.py
	${ENV} ./manim.py dfs.py InOrder ${FLAGS}
	if ${sync}; then aws s3 cp media/$@ s3://manim; fi
	if ${open}; then open $@; fi

videos/dfs/${RES}/PostOrder.mp4: dfs.py logo.py
	${ENV} ./manim.py dfs.py PostOrder ${FLAGS}
	if ${sync}; then aws s3 cp media/$@ s3://manim; fi
	if ${open}; then open $@; fi

validate_sudoku: 	videos/validate_sudoku/${RES}/SudokuValidateColumns.mp4 \
					videos/validate_sudoku/${RES}/SudokuValidateRows.mp4 \
					videos/validate_sudoku/${RES}/RowValidation.mp4 \
					videos/validate_sudoku/${RES}/SudokuValidateSections.mp4
					videos/validate_sudoku/${RES}/SudokuValidateAll.mp4

videos/validate_sudoku/${RES}/SudokuValidateRows.mp4: validate_sudoku.py logo.py sudoku.py
	${ENV} ./manim.py validate_sudoku.py SudokuValidateRows ${FLAGS}
	if ${sync}; then aws s3 cp media/$@ s3://manim; fi
	if ${open}; then open $@; fi

videos/validate_sudoku/${RES}/SudokuValidateColumns.mp4: validate_sudoku.py logo.py  sudoku.py
	${ENV} ./manim.py validate_sudoku.py SudokuValidateColumns ${FLAGS}
	if ${sync}; then aws s3 cp media/$@ s3://manim; fi
	if ${open}; then open $@; fi

videos/validate_sudoku/${RES}/SudokuValidateSections.mp4: validate_sudoku.py logo.py  sudoku.py
	${ENV} ./manim.py validate_sudoku.py SudokuValidateSections ${FLAGS}
	if ${sync}; then aws s3 cp media/$@ s3://manim; fi
	if ${open}; then open $@; fi

videos/validate_sudoku/${RES}/SudokuValidateAll.mp4: validate_sudoku.py logo.py  sudoku.py
	${ENV} ./manim.py validate_sudoku.py SudokuValidateAll ${FLAGS}
	if ${sync}; then aws s3 cp media/$@ s3://manim; fi
	if ${open}; then open $@; fi

videos/validate_sudoku/${RES}/RowValidation.mp4: validate_sudoku.py logo.py sudoku.py
	${ENV} ./manim.py validate_sudoku.py RowValidation ${FLAGS}
	if ${sync}; then aws s3 cp media/$@ s3://manim; fi
	if ${open}; then open $@; fi

solve_sudoku: videos/sudoku/${RES}/SudokuCreationScene.mp4 \
			  videos/sudoku/${RES}/SudokuColumns.mp4 \
			  videos/sudoku/${RES}/SudokuRows.mp4 \
			  videos/sudoku/${RES}/SudokuSquares.mp4 \
			  videos/sudoku/${RES}/SolveSudoku.mp4 \
			  videos/sudoku/${RES}/SudokuLinearScan.mp4

videos/sudoku/${RES}/SudokuLinearScan.mp4: sudoku.py logo.py
	${ENV} ./manim.py sudoku.py SudokuLinearScan ${FLAGS}
	if ${sync}; then aws s3 cp media/$@ s3://manim; fi
	if ${open}; then open $@; fi

videos/sudoku/${RES}/SolveSudoku.mp4: sudoku.py logo.py
	${ENV} ./manim.py sudoku.py SolveSudoku ${FLAGS}
	if ${sync}; then aws s3 cp media/$@ s3://manim; fi
	if ${open}; then open $@; fi

videos/sudoku/${RES}/SudokuCreationScene.mp4: sudoku.py logo.py
	${ENV} ./manim.py sudoku.py SudokuCreationScene ${FLAGS}
	if ${sync}; then aws s3 cp media/$@ s3://manim; fi
	if ${open}; then open $@; fi

videos/sudoku/${RES}/SudokuColumns.mp4: sudoku.py logo.py
	${ENV} ./manim.py sudoku.py SudokuColumns ${FLAGS}
	if ${sync}; then aws s3 cp media/$@ s3://manim; fi
	if ${open}; then open $@; fi

videos/sudoku/${RES}/SudokuRows.mp4: sudoku.py logo.py
	${ENV} ./manim.py sudoku.py SudokuRows ${FLAGS}
	if ${sync}; then aws s3 cp media/$@ s3://manim; fi
	if ${open}; then open $@; fi

videos/sudoku/${RES}/SudokuSquares.mp4: sudoku.py logo.py
	${ENV} ./manim.py sudoku.py SudokuSquares ${FLAGS}
	if ${sync}; then aws s3 cp media/$@ s3://manim; fi
	if ${open}; then open $@; fi

subarray_sum: videos/subarray_sum_equals_k/${RES}/HoppingDownTheRoad.mp4 \
			  videos/subarray_sum_equals_k/${RES}/HoppingBackK.mp4 \
			  videos/subarray_sum_equals_k/${RES}/HoppingBackKSubs.mp4 \

videos/subarray_sum_equals_k/${RES}/HoppingBackK.mp4: subarray_sum_equals_k.py logo.py
	${ENV} ./manim.py subarray_sum_equals_k.py HoppingBackK ${FLAGS}
	if ${sync}; then aws s3 cp media/$@ s3://manim; fi
	if ${open}; then open $@; fi

videos/subarray_sum_equals_k/${RES}/HoppingBackKSubs.mp4: subarray_sum_equals_k.py logo.py
	${ENV} ./manim.py subarray_sum_equals_k.py HoppingBackKSubs ${FLAGS}
	if ${sync}; then aws s3 cp media/$@ s3://manim; fi
	if ${open}; then open $@; fi

videos/subarray_sum_equals_k/${RES}/HoppingDownTheRoad.mp4: subarray_sum_equals_k.py logo.py
	${ENV} ./manim.py subarray_sum_equals_k.py HoppingDownTheRoad ${FLAGS}
	if ${sync}; then aws s3 cp media/$@ s3://manim; fi
	if ${open}; then open $@; fi

primes: 			videos/primes/${RES}/PrimesTrialDivision.mp4 \
			videos/primes/${RES}/PrimesSieve.mp4 \


videos/primes/${RES}/PrimesSieve.mp4: primes.py logo.py
	${ENV} ./manim.py primes.py PrimesSieve ${FLAGS}
	if ${sync}; then aws s3 cp media/$@ s3://manim; fi
	if ${open}; then open $@; fi

videos/primes/${RES}/PrimesTrialDivision.mp4: primes.py logo.py
	${ENV} ./manim.py primes.py PrimesTrialDivision ${FLAGS}
	if ${sync}; then aws s3 cp media/$@ s3://manim; fi
	if ${open}; then open $@; fi

array_index_element: videos/array_index_element/${RES}/ArrayIndexElement.mp4

videos/array_index_element/${RES}/ArrayIndexElement.mp4: array_index_element.py logo.py
	${ENV} ./manim.py array_index_element.py ArrayIndexElement ${FLAGS}
	if ${sync}; then aws s3 cp media/$@ s3://manim; fi
	if ${open}; then open $@; fi

demo: videos/demo/${RES}/Demo.mp4

videos/demo/${RES}/Demo.mp4: demo.py logo.py
	${ENV} ./manim.py demo.py Demo ${FLAGS}
	if ${sync}; then aws s3 cp media/$@ s3://manim; fi
	if ${open}; then open $@; fi

lev: 		videos/levenshtein_distance/${RES}/LevenshteinDistance.mp4 \
			videos/levenshtein_distance/${RES}/LevenshteinDistanceEdits.mp4


videos/levenshtein_distance/${RES}/LevenshteinDistance.mp4: levenshtein_distance.py logo.py
	${ENV} ./manim.py levenshtein_distance.py LevenshteinDistance ${FLAGS}
	if ${sync}; then aws s3 cp media/$@ s3://manim; fi
	if ${open}; then open $@; fi

videos/levenshtein_distance/${RES}/LevenshteinDistanceEdits.mp4: levenshtein_distance.py logo.py
	${ENV} ./manim.py levenshtein_distance.py LevenshteinDistanceEdits ${FLAGS}
	if ${sync}; then aws s3 cp media/$@ s3://manim; fi
	if ${open}; then open $@; fi

islands: 	videos/number_of_islands/${RES}/NumberOfIslandsLinearScan.mp4 \
			videos/number_of_islands/${RES}/NumberOfIslands.mp4 \

videos/number_of_islands/${RES}/NumberOfIslands.mp4: number_of_islands.py logo.py
	${ENV} ./manim.py number_of_islands.py NumberOfIslands ${FLAGS}
	if ${sync}; then aws s3 cp media/$@ s3://manim; fi
	if ${open}; then open $@; fi

videos/number_of_islands/${RES}/NumberOfIslandsLinearScan.mp4: number_of_islands.py logo.py
	${ENV} ./manim.py number_of_islands.py NumberOfIslandsLinearScan ${FLAGS}
	if ${sync}; then aws s3 cp media/$@ s3://manim; fi
	if ${open}; then open $@; fi

celebrity: 	videos/find_the_celebrity/${RES}/CelebrityNaive.mp4 \
			videos/find_the_celebrity/${RES}/CelebrityGraph.mp4 \
			videos/find_the_celebrity/${RES}/CelebrityGraphDFS.mp4 \
			videos/find_the_celebrity/${RES}/CelebrityConfirmation.mp4

videos/find_the_celebrity/${RES}/CelebrityNaive.mp4: find_the_celebrity.py logo.py
	${ENV} ./manim.py find_the_celebrity.py CelebrityNaive ${FLAGS}
	if ${sync}; then aws s3 cp media/$@ s3://manim; fi
	if ${open}; then open $@; fi

videos/find_the_celebrity/${RES}/CelebrityGraph.mp4: find_the_celebrity.py logo.py
	${ENV} ./manim.py find_the_celebrity.py CelebrityGraph ${FLAGS}
	if ${sync}; then aws s3 cp media/$@ s3://manim; fi
	if ${open}; then open $@; fi

videos/find_the_celebrity/${RES}/CelebrityGraphDFS.mp4: find_the_celebrity.py logo.py
	${ENV} ./manim.py find_the_celebrity.py CelebrityGraphDFS ${FLAGS}
	if ${sync}; then aws s3 cp media/$@ s3://manim; fi
	if ${open}; then open $@; fi

videos/find_the_celebrity/${RES}/CelebrityConfirmation.mp4: find_the_celebrity.py logo.py
	${ENV} ./manim.py find_the_celebrity.py CelebrityConfirmation ${FLAGS}
	if ${sync}; then aws s3 cp media/$@ s3://manim; fi
	if ${open}; then open $@; fi

sync:
	rsync --progress ${ALL_VIDS} root@ioloop.io:/home/static/

du:
	du -ach ${ALL_VIDS}

# screensaver:
# 	for vid in ${ALL_VIDS}; do cp $${vid} ${HOME}/collection.media/; done
